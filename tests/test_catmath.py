from catinabox import catmath
import pytest


@pytest.mark.parametrize('age', [
    [10, 50],
    [0.1, 0.5],
    [0, 0],
])
def test__cat_hooman_age_conversion(age):
    assert catmath.cat_years_to_hooman_years(age[0]) == age[1]

# BONUS MATERIAL FOR STEP 2


def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__fails():
    assert catmath.is_cat_leap_year(2015) is False


def test__is_cat_leap_year__2000():
    assert catmath.is_cat_leap_year(2000) is True
