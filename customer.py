from functions import _validate_string


class Customer():
    CUSTOMERS = []

    def __init__(self, new_given_name="defaultGivenName", new_family_name='defaultFamilyName'):
        self._given_name = _validate_string(new_given_name)
        self._family_name = _validate_string(new_family_name)
        self._full_name = None
        self.update_full_name()
        self._full_customer_details = {}
        self._reviewed_restaurants = []
        self.get_customer_details()
        self.add_to_customers_list(self._full_customer_details)

    def get_customer_details(self):
        self._full_customer_details = {
            "given_name": self._given_name,
            "family_name": self._family_name,
            "full_name": self._full_name
        }
        return self._full_customer_details

    @classmethod
    def all_customers(cls):
        return cls.CUSTOMERS

    @staticmethod
    def add_to_customers_list(full_customer):
        Customer.CUSTOMERS.append(full_customer)

    @property
    def family_name(self):
        return self.family_name

    @family_name.setter
    def family_name(self, updated_family_name):
        if isinstance(updated_family_name, str):
            self._family_name = updated_family_name
            self.update_full_name()

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, updated_given_name):
        self._given_name = self._validate_string(updated_given_name)
        self.update_full_name()

    @property
    def full_name(self):
        self.update_full_name()
        return self._full_name

    def update_full_name(self):
        self._full_name = f'{self._family_name.title()}, {self._given_name.title()}'

    @property
    def reviewed_restaurants(self):
        return list(set(self._reviewed_restaurants))

    def add_reviewed_restaurants(self):
        from review import Review
        for review in Review.REVIEWS:
            if review['customer'] == self._full_name and review['restaurant'] not in self._reviewed_restaurants:
                self._reviewed_restaurants.append(review['restaurant'])
        return self._reviewed_restaurants
