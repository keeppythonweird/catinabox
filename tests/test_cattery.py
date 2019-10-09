import pytest

from catinabox import cattery, mccattery


###########################################################################
# add_cats
###########################################################################
@pytest.fixture(params=[cattery, mccattery])
def cattery_client(request):
    return request.param.Cattery()


def test__add_cats__succeeds(cattery_client):
    c = cattery_client
    c.add_cats(["Fluffy", "Snookums"])
    assert c.cats == ["Fluffy", "Snookums"]
    assert c.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(cattery_client):
    c = cattery_client
    c.add_cats(["Fluffy", "Junior"])
    c.remove_cat("Fluffy")
    assert c.cats == ["Junior"]
    assert c.num_cats == 1


def test__remove_cat__no_cats__fails(cattery_client):
    c = cattery_client
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cattery_client):
    c = cattery_client
    c.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("Snookums")
