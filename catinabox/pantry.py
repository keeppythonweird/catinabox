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
        if quantity <= 0:
            raise InvalidQuantity(quantity)
        self._food += [food_type] * quantity

    def list_food(self):
        return copy.copy(self._food)

    def retrieve_food(self, quantity):
        if quantity > len(self._food):
            raise NotEnoughItemsInPantry(len(self._food), quantity)
        retrieved_food = self._food[:quantity]
        self._food = self._food[quantity:]
        return retrieved_food
