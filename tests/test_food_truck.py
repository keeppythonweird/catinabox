import pytest

from catinabox.food_truck import (
    FoodTruck, FoodQuantityCannotBeNegativeError,
)


@pytest.fixture
def food_truck():
    return FoodTruck()


def test_no_food_in_new_food_truck(food_truck):
    assert food_truck.inventory == {}


@pytest.mark.parametrize('food,quantity', (
    ('tacos', 10),
    ('sushi', 1),
    ('curry', 0),
))
def test_stocking_new_food(food_truck, food, quantity):
    food_truck.stock(food, quantity)
    assert food_truck._inventory[food] == quantity


@pytest.mark.parametrize('food,quantity', (
    ('tacos', -10),
    ('sushi', -1337),
    ('curry', -2),
))
def test_stocking_new_food_invalid_quantity(food_truck, food, quantity):
    with pytest.raises(FoodQuantityCannotBeNegativeError):
        food_truck.stock(food, quantity)
