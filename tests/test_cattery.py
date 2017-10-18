import pytest

from catinabox import cattery
from catinabox import mccattery


@pytest.fixture(params=[
                cattery.Cattery,
                mccattery.McCattery
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
    cattery_client.add_cats(["Fluffy", "Snookums"])
    cattery_client.remove_cat("Fluffy")
    assert cattery_client.cats == ["Snookums"]
    assert cattery_client.num_cats == 1


def test__remove_cat__no_cats__fails(cattery_client):
    with pytest.raises(cattery.CatNotFound):
        cattery_client.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cattery_client):
    cattery_client.add_cats(["Fluffy", "Snookums"])
    with pytest.raises(cattery.CatNotFound):
        cattery_client.remove_cat("Fluffles")


def test__mccattery_history__not_empty():
    mcc = mccattery.McCattery()
    mcc.add_cats(["Humblebum", "Mouse"])
    mcc.remove_cat("Humblebum")
    assert len(mcc.history) == 3
