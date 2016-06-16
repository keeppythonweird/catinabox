from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 7
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) is 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


def test__is_cat_leap_year__fails_non_div_4():
    assert catmath.is_cat_leap_year(2015) is False


def test__is_cat_leap_year__fails_div_400():
    assert catmath.is_cat_leap_year(1800) is False


def test__is_cat_leap_year__succeeds_div_400():
    assert catmath.is_cat_leap_year(2000)
