from catinabox import catmath
import pytest


@pytest.fixture(scope='module', params=[12, 13, 22, 100])
def middle(request):
    return request.param


@pytest.fixture(scope='module', params=[.5, .1, .2])
def less_than_1(request):
    return request.param


def test__cat_years_to_hooman_years__middle_age__succeeds(middle):
    assert catmath.cat_years_to_hooman_years(middle) == middle * 5


def test__cat_years_to_hooman_years__less_than_one_year__succeeds(less_than_1):
    assert catmath.cat_years_to_hooman_years(less_than_1) == less_than_1 * 5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2


def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True

    assert catmath.is_cat_leap_year(2015) is False

    assert catmath.is_cat_leap_year(1997) is False

    assert catmath.is_cat_leap_year(1900) is False

    assert catmath.is_cat_leap_year(1600) is True
