import pytest

from catinabox import cattery, mccattery


@pytest.fixture(params=[
    cattery.Cattery,
    mccattery.McCattery,
])
def cattery_client(request):
    return request.param()

###########################################################################
# add_cats
###########################################################################


def test__add_cats__succeeds(cattery_client):
    cattery_client.add_cats(["Fluffy", "Snookums"])
    assert cattery_client.cats == ["Fluffy", "Snookums"]
    assert cattery_client.num_cats == 2


###########################################################################
# remove_cat
###########################################################################


def test__remove_cat__succeeds(cattery_client):
    cattery_client.add_cats(["Fluffy", "Junior"])
    cattery_client.remove_cat("Fluffy")
    assert cattery_client.cats == ["Junior"]
    assert cattery_client.num_cats == 1


def test__remove_cat__no_cats__fails(cattery_client):
    with pytest.raises(cattery.CatNotFound):
        cattery_client.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cattery_client):
    cattery_client.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        cattery_client.remove_cat("Snookums")


###########################################################################
# history (McCattery only)
###########################################################################


def test__mccattery_history(cattery_client):
    if type(cattery_client) is mccattery.McCattery:
        cattery_client.add_cats(["Fluffy", "Junior"])
        cattery_client.remove_cat("Fluffy")
        history = cattery_client.history
        assert history[0].startswith("Added 'Fluffy'")
        assert history[1].startswith("Added 'Junior'")
        assert history[2].startswith("Removed 'Fluffy'")
