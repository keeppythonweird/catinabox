import pytest

from catinabox import safecatmath


@pytest.mark.parametrize('cat_age, hooman_age', [
    (7, 35),
    (0.1, 0.5),
    (0, 0)
])
def test__cat_years_to_hooman_years(cat_age, hooman_age):
    assert safecatmath.cat_years_to_hooman_years(cat_age) == hooman_age


@pytest.mark.parametrize('cat_age', [
    -1,
    10001,
    'test',
    [-3, 4],
    {3: 4},
    float('nan')
])
def test__cat_years_to_hooman_years_invalid_raises(cat_age):
    with pytest.raises(safecatmath.InvalidAge):
        safecatmath.cat_years_to_hooman_years(cat_age)
