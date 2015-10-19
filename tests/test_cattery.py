import pytest

from catinabox import cattery


@pytest.fixture(scope='module')
def my_fixture():
    c = cattery.Cattery()
    c.add_cats(["Fluffy", "Snookums"])
    return c


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(my_fixture):
    assert my_fixture.cats == ["Fluffy", "Snookums"]
    assert my_fixture.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(my_fixture):
    my_fixture.remove_cat("Fluffy")
    assert my_fixture.cats == ["Snookums"]
    assert my_fixture.num_cats == 1


def test__remove_cat__no_cats__fails(my_fixture):
    with pytest.raises(cattery.CatNotFound):
        my_fixture.remove_cat("CatUnknown")


def test__remove_cat__cat_not_in_cattery__fails(my_fixture):
    with pytest.raises(cattery.CatNotFound):
        my_fixture.remove_cat("CatUnknown")
