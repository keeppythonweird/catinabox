import pytest

from catinabox import safecatmath


@pytest.mark.parametrize('age', [
    [7, 35],
    [0.1, 0.5],
    [0, 0]
])
def test__cat_hooman_age_conversion(age):
    assert safecatmath.cat_years_to_hooman_years(age[0]) == age[1]


@pytest.mark.parametrize('cat_age', [-1, 9000, 'cats!', float('nan')])
def test__cat_hooman_age_conversion__raises(cat_age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(cat_age)
