from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    expected_hooman_years = 50
    assert catmath.cat_years_to_hooman_years(10) == expected_hooman_years


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    expected_hooman_years = 0.5
    assert catmath.cat_years_to_hooman_years(0.1) == expected_hooman_years


def test__cat_years_to_hooman_years__0__returns_0():
    expected_hooman_years = 0
    assert catmath.cat_years_to_hooman_years(0) == expected_hooman_years


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__succeeds2():
    assert catmath.is_cat_leap_year(400) is True


def test__is_cat_leap_year__fails1():
    assert catmath.is_cat_leap_year(2019) is False


def test__is_cat_leap_year__fails2():
    assert catmath.is_cat_leap_year(200) is False
