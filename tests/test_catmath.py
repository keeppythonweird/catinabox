import pytest
from catinabox import catmath


@pytest.mark.parametrize('age, expected', [
    (7, 35),
    (8.7, 43.5),
    (11.0, 55.0),
])
def test__cat_years_to_hooman_years__middle_age__succeeds(age, expected):
    assert catmath.cat_years_to_hooman_years(age) == expected


@pytest.mark.parametrize('age, expected', [
    (0.7, 3.5),
    (0.02, 0.1),
])
def test__cat_years_to_hooman_years__less_than_one_year__succeeds(
    age, expected
):
    assert catmath.cat_years_to_hooman_years(age) == expected


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0
