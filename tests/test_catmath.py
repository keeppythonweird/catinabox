from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    expected = 50
    result = catmath.cat_years_to_hooman_years(10)
    assert expected == result


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    expected = 2.5
    result = catmath.cat_years_to_hooman_years(0.5)
    assert expected == result


def test__cat_years_to_hooman_years__0__returns_0():
    expected = 0
    result = catmath.cat_years_to_hooman_years(0)
    assert expected == result


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(3) is False
    assert catmath.is_cat_leap_year(2016) is True
    assert catmath.is_cat_leap_year(4) is True
    assert catmath.is_cat_leap_year(100) is False
    assert catmath.is_cat_leap_year(400) is True
