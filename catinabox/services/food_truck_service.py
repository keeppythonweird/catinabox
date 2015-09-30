from .util import http


class FoodTruckService(object):

    name = 'foodtruck'
    _inventory = {}

    @http('GET', '/')
    def index(self, request):
        return 200, 'Welcome to the food truck!'
