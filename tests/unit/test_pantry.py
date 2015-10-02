import pytest

from catinabox import pantry


class TestPantry(object):

    ###########################################################################
    # add_food
    ###########################################################################

    def test__add_food__succeeds(self):
        p = pantry.Pantry()
        assert p.list_food() == []
        p.add_food('high quality crisps', 2)
        assert p.list_food() == ['high quality crisps', 'high quality crisps']

    def test__add_food__quantity_0__raises(self):
        p = pantry.Pantry()
        with pytest.raises(pantry.InvalidQuantity):
            p.add_food(food_type="liver", quantity=0)

    def test__add_food__quantity_less_than_0__raises(self):
        p = pantry.Pantry()
        with pytest.raises(pantry.InvalidQuantity):
            p.add_food(food_type="liver", quantity=-10)

    ###########################################################################
    # list_food
    ###########################################################################

    def test__list_food__food_in_pantry__returns_all_food(self):
        p = pantry.Pantry()
        p.add_food(food_type="burger", quantity=3)
        p.add_food(food_type="pancake", quantity=4)
        assert p.list_food() == ["burger",
                                 "burger",
                                 "burger",
                                 "pancake",
                                 "pancake",
                                 "pancake",
                                 "pancake"]

    def test__list_food__no_food_in_pantry__returns_nothing(self):
        p = pantry.Pantry()
        assert p.list_food() == []

    ###########################################################################
    # retrieve_food
    ###########################################################################

    def test__retrieve_food__food_in_pantry__removes_and_returns(self):
        p = pantry.Pantry()
        p.add_food(food_type="pickle", quantity=1)
        p.add_food(food_type="bacon", quantity=2)
        p.add_food(food_type="tuna", quantity=3)
        assert p.retrieve_food(quantity=4) == ["pickle",
                                               "bacon",
                                               "bacon",
                                               "tuna"]
        assert p.list_food() == ["tuna", "tuna"]

    def test__retrieve_food__all_food_in_pantry__removes_and_returns(self):
        p = pantry.Pantry()
        p.add_food(food_type="bacon", quantity=2)
        assert p.retrieve_food(quantity=2) == ["bacon", "bacon"]
        assert p.list_food() == []

    def test__retrieve_food__no_food_in_pantry__fails(self):
        p = pantry.Pantry()
        with pytest.raises(pantry.NotEnoughItemsInPantry):
            p.retrieve_food(quantity=1)

    def test__retrieve_food__not_enough_food_in_pantry__fails(self):
        p = pantry.Pantry()
        with pytest.raises(pantry.NotEnoughItemsInPantry):
            p.retrieve_food(quantity=1)
