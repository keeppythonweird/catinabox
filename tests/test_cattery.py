import pytest

from catinabox import cattery
from catinabox import mccattery


@pytest.fixture(params=[cattery.Cattery, mccattery.McCattery])
def ctry(request):
    return request.param()


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(ctry):
    ctry.add_cats(["Fluffy", "Snookums"])
    assert ctry.cats == ["Fluffy", "Snookums"]
    assert ctry.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(ctry):
    ctry.add_cats(["Fluffy", "Junior"])
    ctry.remove_cat("Fluffy")
    assert ctry.cats == ["Junior"]
    assert ctry.num_cats == 1


def test__remove_cat__no_cats__fails(ctry):
    with pytest.raises(cattery.CatNotFound):
        ctry.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(ctry):
    ctry.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        ctry.remove_cat("Snookums")


###########################################################################
# history
###########################################################################

def test__add_cats_history__succeeds():
    cat = mccattery.McCattery()
    cat.add_cats(["Fluffy", "Snookums"])
    assert len(cat.history) == 2


def test__remove_cats_history__succeeds():
    cat = mccattery.McCattery()
    cat.add_cats(["Fluffy", "Snookums"])
    cat.remove_cat("Fluffy")
    assert len(cat.history) == 3
