from customer import customer1
from restaurant import restaurant1
from functions import _validate_int


class Review:
    REVIEWS = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = _validate_int(rating)
        self._review_details = {}
        self.get_review_details()
        self.update_reviews(self._review_details)

    def rating(self):
        return self._rating

    def get_review_details(self):
        if self._rating is None or self._customer.full_name is None or self._restaurant.name is None:
            print("Error! Ensure all values are set.")
            return
        else:
            self._review_details = {
                "customer": self._customer.full_name,
                "restaurant": self._restaurant.name,
                "rating": self._rating
            }
        return self._review_details

    def update_reviews(self,review):
        self.REVIEWS.append(review)

    @classmethod
    def all_reviews(cls):
        return cls.REVIEWS



review1 = Review(customer1, restaurant1, 10)
review1 = Review(customer1, restaurant1, 12)
review1 = Review(customer1, restaurant1, 13)
print(Review.all_reviews())


