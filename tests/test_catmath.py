from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(7) == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__fails():
    assert catmath.is_cat_leap_year(2015) is False


def test__is_cat_leap_year__100():
    assert catmath.is_cat_leap_year(1000) is False


def test__is_cat_leap_year__400():
    assert catmath.is_cat_leap_year(2400) is True
