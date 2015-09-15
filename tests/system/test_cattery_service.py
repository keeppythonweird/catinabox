import pytest
import requests


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

    def delete(self, *args, **kwargs):
        return requests.delete("{base_url}/{url_parts}".format(
            base_url=self._base_url, url_parts="/".join(args)
        ), **kwargs)





@pytest.yield_fixture
def cattery_client():
    # start the service
    yield HttpBaseClient("http://localhost:8000")
    # stop the service



def test__get_all_cats__no_cats__returns_no_cats(cattery_client):
    result = cattery_client.get("cats")
    assert result.json() == []
    assert result.status_code == 200
