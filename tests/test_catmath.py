from catinabox.catmath import cat_years_to_hooman_years, is_cat_leap_year


def test__cat_years_to_hooman_years__middle_age__succeeds():
    catage = 10
    hooman_age = cat_years_to_hooman_years(catage)
    assert hooman_age == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    catage = 0.3
    hooman_age = cat_years_to_hooman_years(catage)
    assert hooman_age == 1.5


def test__cat_years_to_hooman_years__0__returns_0():
    catage = 0
    hooman_age = cat_years_to_hooman_years(catage)
    assert hooman_age == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__is_leap_year():
    assert is_cat_leap_year(2016) is True


def test__is_cat_leap_year__not_divisible_by_4_is_not_leap_year():
    assert is_cat_leap_year(1999) is False


def test__is_cat_leap_year__divisible_by_100_is_not_leap_year():
    assert is_cat_leap_year(1900) is False


def test__is_cat_leap_year__centurial_leap_year__is_leap_year():
    assert is_cat_leap_year(2000) is True
