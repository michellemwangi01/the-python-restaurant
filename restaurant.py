from functions import _validate_string


class Restaurant:
    def __init__(self, name="defaultRestaurantName"):
        self._name = _validate_string(name)

    @property
    def name(self):
        return self._name


restaurant1 = Restaurant("Hibbs")
# print(restaurant1.name)

