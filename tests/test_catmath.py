import pytest
from catinabox import catmath

@pytest.mark.parametrize("cat_years,hooman_years", [(10, 50), (0.5, 2.5), (0,0)])


def test__cat_years_to_hooman_years(cat_years, hooman_years):
    assert catmath.cat_years_to_hooman_years(cat_years) == hooman_years


"""
def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(10) == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0
"""

# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year_not_div_4():
    assert catmath.is_cat_leap_year(2017) is False


def test__is_cat_leap_year_div_4_not_div_100():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year_div_4_div_100_not_div_400():
    assert catmath.is_cat_leap_year(2100) is False


def test__is_cat_leap_year_div_4_div_100_div_400():
    assert catmath.is_cat_leap_year(2000) is True
