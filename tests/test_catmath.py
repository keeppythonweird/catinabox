from catinabox import catmath
import pytest


@pytest.mark.parametrize(('tc', 'expct'), [
    (6, 30),
    (5, 25),
    (4, 20),
    (10, 50)
])
def test__cat_years_to_hooman_years__middle_age__succeeds(tc, expct):
    assert catmath.cat_years_to_hooman_years(tc) == expct


@pytest.mark.parametrize(('tc', 'expct'), [
    (.5, .5 * catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR),
    (.75, .75 * catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR),
    (.45, .45 * catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR)
])
def test__cat_years_to_hooman_years__less_than_one_year__succeeds(tc, expct):
    assert catmath.cat_years_to_hooman_years(tc) == expct


@pytest.mark.parametrize(('tc', 'expct'), [
    (0, 0),
])
def test__cat_years_to_hooman_years__0__returns_0(tc, expct):
    assert catmath.cat_years_to_hooman_years(tc) == expct


# BONUS MATERIAL FOR STEP 2
def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
