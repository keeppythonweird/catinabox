from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    hooman_years = catmath.cat_years_to_hooman_years(7)
    assert hooman_years == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    hooman_years = catmath.cat_years_to_hooman_years(.5)
    assert hooman_years == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_years = catmath.cat_years_to_hooman_years(0)
    assert hooman_years == 0


# BONUS MATERIAL FOR STEP 2

def test__2016_is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__2000_is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2000) is True


def test__1900_is_not_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(1900) is False


def test__2001_is_not_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2001) is False
