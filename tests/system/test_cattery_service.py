import json
import pytest

from util import HttpBaseClient, start_service


@pytest.yield_fixture
def cattery_client():
    # start the service
    service = start_service('catinabox.services.cattery')
    yield HttpBaseClient("http://localhost:8000")
    service.terminate()
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
