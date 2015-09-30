import requests
import shlex
import subprocess
import time

import pytest


class HttpBaseClient(object):

    def __init__(self, base_url):
        self._base_url = base_url

    def get(self, *args, **kwargs):
        return requests.get("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)

    def post(self, *args, **kwargs):
        return requests.post("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)

    def patch(self, *args, **kwargs):
        return requests.patch("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)

    def delete(self, *args, **kwargs):
        return requests.delete("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)


@pytest.fixture
def http_port():
    return 8000


@pytest.yield_fixture
def start_services(http_port):
    cmd = 'nameko run catinabox.services.cattery_service'
    process = subprocess.Popen(shlex.split(cmd))
    yield process
    process.terminate()
    process.wait()


@pytest.fixture
def make_http_client(start_services, http_port):
    def make_client(base_path):
        client = HttpBaseClient(
            'http://localhost:{}/{}'.format(http_port, base_path))
        for _ in range(10):
            try:
                resp = client.get('')
                if resp.status_code == 200:
                    break
            except requests.exceptions.ConnectionError:
                pass
            time.sleep(0.1)
        else:
            pytest.fail('Unable to connect to the services')
        return client
    return make_client


@pytest.fixture
def cattery_client(make_http_client):
    return make_http_client('')


@pytest.fixture
def foodtruck_client(make_http_client):
    return make_http_client('foodtruck')
