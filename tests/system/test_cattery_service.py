import json
import pytest
import requests
import time

from util import HttpBaseClient, start_service


@pytest.yield_fixture
def cattery_client():
    # start the service
    service = start_service('catinabox.services.cattery')
    client = HttpBaseClient("http://localhost:8000")
    for _ in range(10):
        try:
            resp = client.get('')
            if resp.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    else:
        pytest.fail('Unable to connect to cattery service')

    yield client
    service.terminate()
    service.wait()
    # stop the service


class TestGetCats(object):

    def test__get_cats__no_cats__returns_no_cats(self, cattery_client):
        result = cattery_client.get('cats')
        assert result.json() == []
        assert result.status_code == 200

    def test__get_cats__cat_added__returns_the_cats(self, cattery_client):
        cattery_client.post('cats', data=json.dumps({"name": "Theodora"}))
        result = cattery_client.get('cats')

        assert result.json() == [{"name": "Theodora"}]
        assert result.status_code == 200
