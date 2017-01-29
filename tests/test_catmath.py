import pytest
from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 10
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.5
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0


def test_int_cat_years_string_raises():
    with pytest.raises(ValueError):
        catmath.int_cat_years('five')


def test_int_cat_years_succeeds():
    assert catmath.int_cat_years(10) == 50


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__not_divisible_by_4__isnt_leap_year():
    assert catmath.is_cat_leap_year(1757) is False


def test__is_cat_leap_year__divisible_by_100__isnt_leap_year():
    assert catmath.is_cat_leap_year(1900) is False


def test__is_cat_leap_year__centurial_leap_year__is_leap_year():
    assert catmath.is_cat_leap_year(2000) is True


def test__is_cat_leap_year__typical_leap_year__is_leap_year():
    assert catmath.is_cat_leap_year(2004) is True
