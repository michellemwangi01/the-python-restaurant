from functions import _validate_string


class Restaurant:
    def __init__(self, name="defaultRestaurantName"):
        self._name = _validate_string(name)
        self._reviews = []
        self._restaurant_reviews_list = []


    @property
    def name(self):
        return self._name

    def add_review(self, reviews):
        for review in reviews:
            if review.restaurant == self._name:
                self._restaurant_reviews_list.append(review)
            else:
                print("Error! This review does not belong to this restaurant.")

    @property
    def restaurant_reviews(self):
        from review import Review
        review_detailed_list = [Review.get_review_details(review) for review in self._restaurant_reviews_list ]
        return review_detailed_list

    def customers_with_reviews(self):
        all_reviews = self.restaurant_reviews
        all_customers = [review['customer'] for review in all_reviews]
        return list(set(all_customers))

