import pytest

from catinabox import cattery, mccattery


@pytest.fixture(params=[
    cattery.Cattery,
    mccattery.McCattery
])
def cats(request):
    return request.param()

###########################################################################
# add_cats
###########################################################################


def test__add_cats__succeeds(cats):
    cats.add_cats(["Fluffy", "Snookums"])
    assert cats.cats == ["Fluffy", "Snookums"]
    assert cats.num_cats == 2

###########################################################################
# remove_cat
###########################################################################


def test__remove_cat__succeeds(cats):
    cats.add_cats(["Fluffy", "Junior"])
    cats.remove_cat("Fluffy")
    assert cats.cats == ["Junior"]
    assert cats.num_cats == 1


def test__remove_cat__no_cats__fails(cats):
    with pytest.raises(cattery.CatNotFound):
        cats.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(cats):
    cats.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        cats.remove_cat("Snookums")


###########################################################################
# history
###########################################################################

def test__history_no_cats(cats):
    if hasattr(cats, "history"):
        assert len(cats.history) == 0


def test__history_cats_added(cats):
    if hasattr(cats, "history"):
        cats.add_cats(["Fluffy"])
        assert len(cats.history) == 1
        cats.add_cats(["Junior"])
        assert len(cats.history) == 2


def test__history_cats_added_removed(cats):
    if hasattr(cats, "history"):
        cats.add_cats(["Fluffy"])
        assert len(cats.history) == 1
        cats.remove_cat("Fluffy")
        assert len(cats.history) == 2
