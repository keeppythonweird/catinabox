import requests
import shlex
import subprocess
import time
import yaml

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


@pytest.yield_fixture
def start_services(tmpdir):
    cattery_config = tmpdir.join('cattery.yml')
    cattery_config.write(
        yaml.dump({'WEB_SERVER_ADDRESS': 'localhost:8080'}))
    food_truck_config = tmpdir.join('food_truck.yml')
    food_truck_config.write(
        yaml.dump({'WEB_SERVER_ADDRESS': 'localhost:8081'}))

    cattery_cmd = ('nameko run --config={} '
                   'catinabox.services.cattery_service')
    cattery = subprocess.Popen(
        shlex.split(cattery_cmd.format(str(cattery_config))))

    food_truck_cmd = ('nameko run --config={} '
                      'catinabox.services.food_truck_service')
    food_truck = subprocess.Popen(
        shlex.split(food_truck_cmd.format(str(food_truck_config))))

    yield

    cattery.terminate()
    food_truck.terminate()
    cattery.wait()
    food_truck.wait()


@pytest.fixture
def make_http_client(start_services):
    def make_client(http_port, base_path=''):
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
    return make_http_client(8080)


@pytest.fixture
def food_truck_client(make_http_client):
    return make_http_client(8081)
