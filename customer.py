import re
from functions import _validate_string



class Customer:
    CUSTOMERS = []

    def __init__(self, new_given_name="defaultGivenName", new_family_name='defaultFamilyName'):
        self._customer_reviews_count = 0
        self._given_name = _validate_string(new_given_name)
        self._family_name = _validate_string(new_family_name)
        self._full_name = None
        self.update_full_name()
        self._full_customer_details = {}
        self._reviewed_restaurants = []
        self._reviews = []
        self.get_customer_details()
        self.add_to_customers_list(self._full_customer_details)

    @property
    def customer_reviews_total(self):
        reviews = self.reviews()
        review_count = len(reviews)
        return f'Total reviews for {self._family_name} {self._given_name} is {review_count}.'

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

    @property
    def reviewed_restaurants(self):
        from review import Review
        for review in Review.REVIEWS:
            if review['customer'] == self._full_name and review['restaurant'] not in self._reviewed_restaurants:
                self._reviewed_restaurants.append(review['restaurant'])
        return f'{self._full_name} has reviewed these restaurants: {self._reviewed_restaurants}'

    def reviews(self):
        from review import Review
        for review in Review.REVIEWS:
            if review['customer'] == self._full_name:
                self._reviewed_restaurants.append(review)
        return self._reviewed_restaurants

    def add_review(self, restaurant, rating):
        from review import Review
        Review(self, restaurant, rating)

    @classmethod
    def find_customer_by_full_name(self, search_term):
        full_names = [customer['full_name'] for customer in Customer.CUSTOMERS]
        pattern = re.escape(search_term)
        matches = [item for item in full_names if re.search(pattern, item)]
        return matches

