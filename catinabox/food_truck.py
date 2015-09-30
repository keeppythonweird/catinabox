class FoodDoesNotExistError(Exception):
    """The requested food item does not exist in the inventory."""

    def __init__(self, food):
        super(FoodDoesNotExistError, self).__init__(
            'Food {!r} was not found in the inventory'.format(food))
        self.food = food


class FoodAlreadyStockedError(Exception):
    """The food item is already tracked in the inventory."""

    def __init__(self, food):
        super(FoodAlreadyStockedError, self).__init__(
            'Food {!r} already exists in the inventory')
        self.food = food


class FoodQuantityCannotBeNegativeError(Exception):
    """The food item's quantity has gone negative."""

    def __init__(self, food, desired):
        super(FoodQuantityCannotBeNegativeError, self).__init__(
            'Food {!r} tried to have a quantity of {!r}'.format(food,
                                                                desired))
        self.food = food
        self.desired = desired


class FoodTruck(object):

    def __init__(self):
        self._inventory = {}

    @property
    def inventory(self):
        return self._inventory

    def stock(self, food, quantity):
        """Add a new food item to the inventory.

        Args:
            food - name of the food item (string)
            quantity - amount of food to stock initially (integer)

        """
        if food in self._inventory:
            raise FoodAlreadyStockedError(food)

        if quantity < 0:
            raise FoodQuantityCannotBeNegativeError(food, quantity)

        self._inventory[food] = quantity

    def restock(self, food, quantity):
        """Update the quantity of food in the inventory.

        Args:
            food - name of the food item (string)
            quantity - amount of food to restock (integer)

        """
        if quantity < 0:
            raise FoodQuantityCannotBeNegativeError(food, quantity)

        try:
            self._inventory[food] = quantity
        except KeyError:
            raise FoodDoesNotExistError(food)

    def discontinue(self, food):
        """Remove a food item from the inventory.

        Args:
            food - name of the food item (string)

        """
        try:
            del self._inventory[food]
        except KeyError:
            raise FoodDoesNotExistError(food)

    def get(self, food):
        """Get the current quantity of a food item from the inventory.

        Args:
            food - name of the food item (string)

        Return: the quantity of the food item (integer)

        """
        try:
            return self._inventory[food]
        except KeyError:
            raise FoodDoesNotExistError(food)

    def consume(self, food, quantity):
        """Consume some quantity of a food item from the inventory.

        Args:
            food - name of the food item (string)
            quantity - amount of food to be consumed (integer)

        """
        stock = self.get(food)
        if stock - quantity < 0:
            raise FoodQuantityCannotBeNegativeError(food, stock - quantity)
        else:
            self.restock(food, stock - quantity)
