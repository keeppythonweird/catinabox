from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(10) == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__2016():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__2013():
    assert catmath.is_cat_leap_year(2013) is False


def test__is_cat_leap_year__2100():
    assert catmath.is_cat_leap_year(2100) is False


def test__is_cat_leap_year__2000():
    assert catmath.is_cat_leap_year(2000) is True
