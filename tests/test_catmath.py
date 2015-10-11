from catinabox import catmath
# import pytest


def test__cat_years_to_hooman_years__middle_age__succeeds():
    loop_results = []
    for x in range(6, 100, 1):
        loop_results.append(catmath.cat_years_to_hooman_years(x) >= 30)

    if sum(loop_results) == len(loop_results):
        assert True
    else:
        assert False


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    loop_results = []
    for x in [element * 0.1 for element in range(0, 10)]:
        loop_results.append(catmath.cat_years_to_hooman_years(x) < 5)

    if sum(loop_results) == len(loop_results):
        assert True
    else:
        assert False


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0
