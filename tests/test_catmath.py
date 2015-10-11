from catinabox.catmath import cat_years_to_hooman_years


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert cat_years_to_hooman_years(3) == 15


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert cat_years_to_hooman_years(.5) == 2.5


def test__cat_years_to_hooman_years__0__returns_0():
    assert cat_years_to_hooman_years(0) == 0
