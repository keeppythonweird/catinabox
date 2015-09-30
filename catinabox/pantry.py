import copy


class InvalidQuantity(Exception):
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return "Quantity must be greater than 0, but was {quantity}".format(
            quantity = self.quantity
        )


class NotEnoughItemsInPantry(Exception):
    def __init__(self, pantry_quantity, requested_quantity):
        self.pantry_quantity = pantry_quantity
        self.requested_quantity = requested_quantity

    def __str__(self):
        return ("Requested {requested_quantity} items, but only "
                "{pantry_quantity} items in pantry.".format(
            requested_quantity=self.requested_quantity,
            pantry_quantity=self.pantry_quantity
        ))


class Pantry(object):
    def __init__(self):
        self._food = []

    def add_food(self, food_type, quantity):
        """Add the specified food to the pantry, in the specified quantity.

        :param food_type: A string, in singular, identifying the food to add.
        :param quantity: The number of food items of the specified type to add.
        """
        if quantity <= 0:
            raise InvalidQuantity(quantity)
        self._food += [food_type] * quantity

    def list_food(self):
        """Get a list of the foods in the pantry.

        :return: A copy of the list of all food items in the pantry.
        """
        return copy.copy(self._food)

    def retrieve_food(self, quantity):
        """Retrieve the specified number of food items from the pantry.

        Items in the pantry are retrieved FIFO.

        :param quantity: The number of food items to retrieve.
        :return: A list of food items. Each item in the list is a string
                 identifying the type of the food item.
        """
        if quantity > len(self._food):
            raise NotEnoughItemsInPantry(len(self._food), quantity)
        retrieved_food = self._food[:quantity]
        self._food = self._food[quantity:]
        return retrieved_food
