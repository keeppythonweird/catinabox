
from catinabox import catmath
from catinabox.catmath import NUM_HOOMAN_YEARS_IN_CAT_YEAR

CY = NUM_HOOMAN_YEARS_IN_CAT_YEAR


def test__cat_years_to_hooman_years__middle_age__succeeds():
    age = 50
    assert catmath.cat_years_to_hooman_years(age) == CY * age


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    age = 0.5
    assert catmath.cat_years_to_hooman_years(age) == CY * age


def test__cat_years_to_hooman_years__0__returns_0():
    age = 0
    assert catmath.cat_years_to_hooman_years(age) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
    assert catmath.is_cat_leap_year(2012) is True
    assert catmath.is_cat_leap_year(2015) is False
