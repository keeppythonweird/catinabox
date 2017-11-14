from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert 50 == catmath.cat_years_to_hooman_years(10)


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert 1.5 == catmath.cat_years_to_hooman_years(0.3)


def test__cat_years_to_hooman_years__0__returns_0():
    assert 0 == catmath.cat_years_to_hooman_years(0)


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
    assert catmath.is_cat_leap_year(2000) is True
    assert catmath.is_cat_leap_year(1904) is True


def test_is_not_cat_leap_year():
    assert catmath.is_cat_leap_year(2017) is False


def test_is_cat_leap_year_divisible_by_100_suceeds():
    assert catmath.is_cat_leap_year(1900) is False
