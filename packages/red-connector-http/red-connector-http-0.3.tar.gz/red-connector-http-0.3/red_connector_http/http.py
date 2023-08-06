import os
import stat
from copy import deepcopy
import shutil

import requests
import json
import jsonschema
from jsonschema.exceptions import ValidationError
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

DEFAULT_DIRECTORY_MODE = stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH \
                         | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH

_HTTP_METHODS = ['Get', 'Put', 'Post']
_HTTP_METHODS_ENUMS = deepcopy(_HTTP_METHODS) + [m.lower() for m in _HTTP_METHODS] + [m.upper() for m in _HTTP_METHODS]

_AUTH_METHODS = ['Basic', 'Digest']
_AUTH_METHODS_ENUMS = deepcopy(_AUTH_METHODS) + [m.lower() for m in _AUTH_METHODS] + [m.upper() for m in _AUTH_METHODS]

HTTP_SCHEMA = {
    'type': 'object',
    'properties': {
        'url': {'type': 'string'},
        'method': {'enum': _HTTP_METHODS_ENUMS},
        'auth': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'password': {'type': 'string'},
                'method': {'enum': _AUTH_METHODS_ENUMS}
            },
            'additionalProperties': False,
            'required': ['username', 'password']
        },
        'disableSSLVerification': {'type': 'boolean'},
        'mergeAgencyData':  {'type': 'boolean'}
    },
    'additionalProperties': False,
    'required': ['url']
}


def _http_method_func(access, default):
    http_method = access.get('method', default).lower()

    if http_method == 'get':
        return requests.get
    if http_method == 'put':
        return requests.put
    if http_method == 'post':
        return requests.post

    raise Exception('Invalid HTTP method: {}'.format(http_method))


def _auth_method_obj(access):
    if not access.get('auth'):
        return None

    auth = access['auth']
    auth_method = auth.get('method', 'basic').lower()

    if auth_method == 'basic':
        return HTTPBasicAuth(
            auth['username'],
            auth['password']
        )
    if auth_method == 'digest':
        return HTTPDigestAuth(
            auth['username'],
            auth['password']
        )

    raise Exception('Invalid auth method: {}'.format(auth_method))


class Http:
    @staticmethod
    def receive(access, internal):
        http_method_func = _http_method_func(access, 'GET')
        auth_method_obj = _auth_method_obj(access)

        verify = True
        if access.get('disableSSLVerification'):
            verify = False

        r = http_method_func(
            access['url'],
            auth=auth_method_obj,
            verify=verify,
            stream=True
        )
        r.raise_for_status()

        with open(internal['path'], 'wb') as f:
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)

        r.raise_for_status()

    @staticmethod
    def receive_cleanup(internal):
        """
        Removes the given file.

        :param internal: A dictionary containing a path to the file to remove.
        """
        os.remove(internal['path'])

    @staticmethod
    def receive_validate(access):
        try:
            jsonschema.validate(access, HTTP_SCHEMA)
        except ValidationError as e:
            raise Exception(e.context)

    @staticmethod
    def send(access, internal):
        http_method_func = _http_method_func(access, 'POST')
        auth_method_obj = _auth_method_obj(access)

        verify = True
        if access.get('disableSSLVerification'):
            verify = False

        with open(internal['path'], 'rb') as f:
            r = http_method_func(
                access['url'],
                data=f,
                auth=auth_method_obj,
                verify=verify
            )
            r.raise_for_status()

    @staticmethod
    def send_validate(access):
        try:
            jsonschema.validate(access, HTTP_SCHEMA)
        except ValidationError as e:
            raise Exception(e.context)

    @staticmethod
    def build_path(base_path, listing, key):
        """
        Builds a list of string representing urls, which are build by the base_url and the subfiles and subdirectories
        inside the listing. The resulting urls are written to the listing with the key 'complete_url'

        :param base_path: A string containing the base path
        :param listing: A dictionary containing information about the directory structure of the given base_url
        :param key: The key under which the complete url is stored
        """

        for sub in listing:
            path = os.path.join(base_path, sub['basename'])
            sub[key] = path
            if sub['class'] == 'Directory':
                if 'listing' in sub:
                    Http.build_path(path, sub['listing'], key)

    @staticmethod
    def fetch_file(file_path, url, http_method, auth_method, verify=True):
        """
        Fetches the given file. Assumes that the directory in which this file is stored is already present in the local
        filesystem.

        :param file_path: The path where the file content should be stored
        :param url: The url from where to fetch the file
        :param http_method: An function object, which returns a requests result,
        if called with (url, auth=auth_method, verify=verify, stream=True)
        :param auth_method: An auth_method, which can be used as parameter for requests.http_method
        :param verify: A boolean indicating if SSL Certification should be used.

        :raise requests.exceptions.HTTPError: If the HTTP requests could not be resolved correctly.
        """

        r = http_method(
            url,
            auth=auth_method,
            verify=verify,
            stream=True
        )
        r.raise_for_status()

        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)

        r.raise_for_status()

    @staticmethod
    def fetch_directory(listing, http_method, auth_method, verify=True):
        """
        :param listing: A complete listing with complete urls for every containing file.
        :param http_method: An function object, which returns a requests result,
        if called with (url, auth=auth_method, verify=verify, stream=True)
        :param auth_method: An auth_method, which can be used as parameter for requests.http_method
        :param verify: A boolean indicating if SSL Certification should be used.

        :raise requests.exceptions.HTTPError: If a HTTP requests could not be resolved correctly.
        """

        for sub in listing:
            if sub['class'] == 'File':
                Http.fetch_file(sub['complete_path'], sub['complete_url'], http_method, auth_method, verify)
            elif sub['class'] == 'Directory':
                os.mkdir(sub['complete_path'], DEFAULT_DIRECTORY_MODE)
                if 'listing' in sub:
                    Http.fetch_directory(sub['listing'], http_method, auth_method, verify)

    @staticmethod
    def receive_directory(access, internal, listing):
        """
        Fetches a directory from a http server.

        :param access: A dictionary containing access information. Has the following keys.
                       - 'url': The URL pointing to the http directory listing.
                       - 'method': A HTTP Method (for example: 'GET')
        :param internal: A dictionary containing information about where to put the directory content.
        :param listing: Listing of subfiles and subdirectories which are contained by the directory given in access.
                        Specified like a listing in the common workflow language.
        """
        if not listing:
            raise Exception('Connector "{}.{}" needs a not empty listing to work properly'
                            .format(Http.__module__, Http.__name__))

        listing = deepcopy(listing)

        Http.build_path(access['url'], listing, 'complete_url')
        Http.build_path(internal['path'], listing, 'complete_path')

        http_method_func = _http_method_func(access, 'GET')
        auth_method_obj = _auth_method_obj(access)

        verify = True
        if access.get('disableSSLVerification'):
            verify = False

        os.mkdir(internal['path'], DEFAULT_DIRECTORY_MODE)

        Http.fetch_directory(listing, http_method_func, auth_method_obj, verify)

    @staticmethod
    def receive_directory_validate(access):
        try:
            jsonschema.validate(access, HTTP_SCHEMA)
        except ValidationError as e:
            raise Exception(e.context)

    @staticmethod
    def receive_directory_cleanup(internal):
        """
        Removes the given directory.

        :param internal: A dictionary containing a path to the directory to remove.
        """
        shutil.rmtree(internal['path'])


class HttpJson:
    @staticmethod
    def receive(access, internal):
        http_method_func = _http_method_func(access, 'GET')
        auth_method_obj = _auth_method_obj(access)

        verify = True
        if access.get('disableSSLVerification'):
            verify = False

        r = http_method_func(
            access['url'],
            auth=auth_method_obj,
            verify=verify
        )
        r.raise_for_status()
        data = r.json()

        with open(internal['path'], 'wb') as f:
            json.dump(data, f)

    @staticmethod
    def receive_validate(access):
        try:
            jsonschema.validate(access, HTTP_SCHEMA)
        except ValidationError as e:
            raise Exception(e.context)

    @staticmethod
    def receive_cleanup(internal):
        """
        Removes the given file.

        :param internal: A dictionary containing a path to the file to remove.
        """
        os.remove(internal['path'])

    @staticmethod
    def send(access, internal):
        http_method_func = _http_method_func(access, 'POST')
        auth_method_obj = _auth_method_obj(access)

        with open(internal['path']) as f:
            data = json.load(f)

        if access.get('mergeAgencyData') and internal.get('agencyData'):
            for key, val in internal['agencyData'].items():
                data[key] = val

        verify = True
        if access.get('disableSSLVerification'):
            verify = False

        r = http_method_func(
            access['url'],
            json=data,
            auth=auth_method_obj,
            verify=verify
        )
        r.raise_for_status()

    @staticmethod
    def send_validate(access):
        try:
            jsonschema.validate(access, HTTP_SCHEMA)
        except ValidationError as e:
            raise Exception(e.context)


class HttpMockSend(Http):
    @staticmethod
    def send(access, internal):
        pass
