from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 45
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 225


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.5
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0


# BONUS MATERIAL FOR STEP 2
""""Comment to implement travis"""

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True

def test__is_cat_leap_year__divisible_by_100_is_not_leap_year():
    assert catmath.is_cat_leap_year(1800) is False

def test__is_cat_leap_year__not_divisible_by_4_is_not_leap_year():
    assert catmath.is_cat_leap_year(1567) is False

def test__is_cat_leap_year__millenium_leap_year_is_leap_year():
    assert catmath.is_cat_leap_year(2000) is True

def test__is_cat_leap_year__typical_leap_year_is_leap_year():
    assert catmath.is_cat_leap_year(2008)