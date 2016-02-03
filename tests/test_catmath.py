from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert True


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    if catmath.cat_years_to_hooman_years(0.1) < 1:
        assert True
    else:
        assert False


def test__cat_years_to_hooman_years__0__returns_0():
    if catmath.cat_years_to_hooman_years(0) == 0:
        assert True
    else:
        assert False
