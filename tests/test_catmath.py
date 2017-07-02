from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(7) == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.1) == 0.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__fails():
    assert catmath.is_cat_leap_year(1977) is False


def test__is_cat_leap_year__yr_not_divisible_by_4_is_common_year__fails():
    assert catmath.is_cat_leap_year(2013) is False


def test__is_cat_leap_year__yr_div_by_4_not_100_is_leap_year__succeeds():
    assert catmath.is_cat_leap_year(1988) is True


def test__is_cat_leap_year__yr_div_by_4_100_not_400_is_common_year__fails():
    assert catmath.is_cat_leap_year(1900) is False


def test__is_cat_leap_year__yr_div_by_4_100_400_is_leap_year__succeeds():
    assert catmath.is_cat_leap_year(1600) is True
