from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    human_age = catmath.cat_years_to_hooman_years(7)
    assert human_age == 35


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    human_age = catmath.cat_years_to_hooman_years(0.5)
    assert human_age == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    human_age = catmath.cat_years_to_hooman_years(0)
    assert human_age == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True

    for year in [4, 200, 400, 1776, 0, 1, 2, 20000000]:
        if year % 4 != 0:
            assert catmath.is_cat_leap_year(year) is False
        elif year % 100 != 0:
            assert catmath.is_cat_leap_year(year) is True
        elif year % 400 != 0:
            assert catmath.is_cat_leap_year(year) is False
        else:
            assert catmath.is_cat_leap_year(year) is True
