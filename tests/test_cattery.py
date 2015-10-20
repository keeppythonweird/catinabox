import pytest

from catinabox import cattery
from catinabox import mccattery


@pytest.fixture(scope='module', params=["aa", "mc"])
def my_fixture(request):
    if request.param == "mc":
        c = mccattery.McCattery()
    else:
        c = cattery.Cattery()

    c.add_cats(["Fluffy", "Snookums"])
    return c


def test__add_cats__succeeds(my_fixture):
    assert my_fixture.cats == ["Fluffy", "Snookums"]
    assert my_fixture.num_cats == 2

    if isinstance(my_fixture, mccattery.McCattery):
        assert any("Fluffy" in s for s in my_fixture.history)
        assert any("Snookums" in s for s in my_fixture.history)


def test__remove_cat__succeeds(my_fixture):
    my_fixture.remove_cat("Fluffy")
    assert my_fixture.cats == ["Snookums"]
    assert my_fixture.num_cats == 1


def test__remove_cat__no_cats__fails():
    c = cattery.Cattery()
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("CatUnknown")


def test__remove_cat__cat_not_in_cattery__fails(my_fixture):
    with pytest.raises(cattery.CatNotFound):
        my_fixture.remove_cat("CatUnknown")


'''
@pytest.fixture(scope='module')
def my_fixture2():
    mc = mccattery.McCattery()
    mc.add_cats(["mcFluffy", "mcSnookums"])
    return mc


###########################################################################
# add_cats
###########################################################################
def test__add_cats__succeeds(my_fixture, my_fixture2):
    assert my_fixture.cats == ["Fluffy", "Snookums"]
    assert my_fixture.num_cats == 2

    assert my_fixture2.cats == ["mcFluffy", "mcSnookums"]
    assert my_fixture2.num_cats == 2
    assert any("mcFluffy" in s for s in my_fixture2.history)
    assert any("mcSnookums" in s for s in my_fixture2.history)


###########################################################################
# remove_cat
###########################################################################
def test__remove_cat__succeeds(my_fixture, my_fixture2):
    my_fixture.remove_cat("Fluffy")
    assert my_fixture.cats == ["Snookums"]
    assert my_fixture.num_cats == 1

    my_fixture2.remove_cat("mcFluffy")
    assert my_fixture2.cats == ["mcSnookums"]
    assert my_fixture2.num_cats == 1
    assert any("mcFluffy" in s for s in my_fixture2.history)


def test__remove_cat__no_cats__fails():
    c = cattery.Cattery()
    c2 = mccattery.McCattery()

    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("CatUnknown")

    with pytest.raises(cattery.CatNotFound):
        c2.remove_cat("CatUnknown")


def test__remove_cat__cat_not_in_cattery__fails(my_fixture, my_fixture2):
    with pytest.raises(cattery.CatNotFound):
        my_fixture.remove_cat("CatUnknown")

    with pytest.raises(cattery.CatNotFound):
        my_fixture2.remove_cat("CatUnknown")
'''
