from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(4) == 20


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(.1) == .5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0
