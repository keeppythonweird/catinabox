import pytest

from util import HttpBaseClient, start_service


@pytest.yield_fixture
def cattery_client():
    # start the service
    service = start_service('catinabox.services.cattery')
    yield HttpBaseClient("http://localhost:8000")
    service.terminate()
    # stop the service


def test__get_all_cats__no_cats__returns_no_cats(cattery_client):
    result = cattery_client.get("cats")
    assert result.json() == []
    assert result.status_code == 200
