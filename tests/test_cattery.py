import pytest

from catinabox import cattery, mccattery


@pytest.fixture(params=[
    cattery.Cattery,
    mccattery.McCattery
])
def cattery_fixture(request):
    return request.param()


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(cattery_fixture):
    cattery_fixture.add_cats(["Fluffy", "Snookums"])
    assert cattery_fixture.cats == ["Fluffy", "Snookums"]
    assert cattery_fixture.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(cattery_fixture):
    cattery_fixture.add_cats(["Fluffy", "Junior"])
    cattery_fixture.remove_cat("Fluffy")
    assert cattery_fixture.cats == ["Junior"]
    assert cattery_fixture.num_cats == 1


def test__remove_cat__no_cats__fails(cattery_fixture):
    with pytest.raises(cattery.CatNotFound):
        cattery_fixture.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cattery_fixture):
    cattery_fixture.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        cattery_fixture.remove_cat("Snookums")
