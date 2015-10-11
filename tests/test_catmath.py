from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    hooman_age = catmath.cat_years_to_hooman_years(8)
    assert hooman_age == (8 * 5)


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    hooman_age = catmath.cat_years_to_hooman_years(0.3)
    assert hooman_age == (0.3 * 5)


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_age = catmath.cat_years_to_hooman_years(0)
    assert hooman_age == 0
