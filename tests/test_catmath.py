from catinabox import catmath

HY_IN_CY = catmath.NUM_HOOMAN_YEARS_IN_CAT_YEAR


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(35) == 35 * HY_IN_CY


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 0.5 * HY_IN_CY


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__1():
    assert catmath.is_cat_leap_year(2017) is False


def test__is_cat_leap_year__2():
    assert catmath.is_cat_leap_year(2018) is False


def test__is_cat_leap_year__3():
    assert catmath.is_cat_leap_year(2019) is False


def test__is_cat_leap_year__4():
    assert catmath.is_cat_leap_year(2020) is True


def test__is_cat_leap_year__century():
    assert catmath.is_cat_leap_year(1900) is False


def test__is_cat_leap_year__400():
    assert catmath.is_cat_leap_year(2400) is True
