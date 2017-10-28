from catinabox.catmath import cat_years_to_hooman_years, is_cat_leap_year


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert cat_years_to_hooman_years(10) == 50


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert cat_years_to_hooman_years(0.3) == 1.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert is_cat_leap_year(2016) is True
