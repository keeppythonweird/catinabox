import pytest

from catinabox import cattery, mccattery


@pytest.fixture(params=[
    cattery.Cattery,
    mccattery.McCattery,
])
def cattery_client(request):
    return request.param()


def test__add_cats__succeeds(cattery_client):
    cattery_client.add_cats(["First", "Second"])
    assert cattery_client.cats == ["First", "Second"]
    assert cattery_client.num_cats == 2


def test__remove_cats__succeeds(cattery_client):
    cattery_client.add_cats(["First", "Second", "Third"])
    cattery_client.remove_cat("Second")
    cattery_client.remove_cat("First")
    assert cattery_client.cats == ["Third"]
    assert cattery_client.num_cats == 1


def test__remove_cat__no_cats__fails(cattery_client):
    with pytest.raises(cattery.CatNotFound):
        cattery_client.remove_cat("First")


def test__remove_cat__cat_not_in_cattery__fails(cattery_client):
    cattery_client.add_cats(["Second"])
    with pytest.raises(cattery.CatNotFound):
        cattery_client.remove_cat("First")


# def test__history():
#     test_mccattery = mccattery.McCattery()
#     test_mccattery.add_cats(["Jerry"])
#     assert len(test_mccattery.history) == 1
