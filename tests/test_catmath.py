from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 7
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.1
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0.5


def test__cat_years_to_hooman_years__0__returns_0():
    cat_age = 0.0
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0.0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
    assert catmath.is_cat_leap_year(2015) is False
    assert catmath.is_cat_leap_year(2000) is True
    assert catmath.is_cat_leap_year(1900) is False
