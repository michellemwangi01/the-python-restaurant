class Review:
    REVIEW_LIST = []

    def __init__(self, customer, restaurant, rating):
        # imported function from Customer
        from customer import Customer
        from restaurant import Restaurant
        self._customer = Customer.full_name(customer)
        # imported functions form Restaurant
        self._restaurant = Restaurant.get_name(restaurant)
        self._rating = Review.validate_integer(rating)
        self.creat_review_object(self)

        # self.get = Restaurant.get_data_from_review(Review.REVIEW_LIST)

    # ----------------------------------------------------------------------------------
    # method to validate if the rating is an integer or not
    @staticmethod
    def validate_integer(rating):
        if isinstance(rating, int):
            return rating
        else:
            return "rating should be an integer"

    # ----------------------------------------------------------------------------------
    # return the rating for  rating for a restaurant
    @property
    def rating(self):
        return self._rating

    # set the rating, user can changer the raiting they gave
    @rating.setter
    def rating(self, rating_value):
        self._rating = rating_value

    # ----------------------------------------------------------------------------------
    # creates the reviw object using the customer , restaurant and  rating details
    @classmethod
    def creat_review_object(cls, self):
        review_object = {
            "full_name": self._customer,
            "restaurant_name": self._restaurant,
            "rating": self._rating,
        }
        Review.add_review_to_list(review_object)

    # ----------------------------------------------------------------------------------
    # adds the review object to the review_list
    @classmethod
    def add_review_to_list(cls, object):
        if object not in cls.REVIEW_LIST:
            cls.REVIEW_LIST.append(object)
        else:
            return cls.REVIEW_LIST

    # ----------------------------------------------------------------------------------
    # return a list of all the review details, customr, restaurant, rating
    @classmethod
    def print_all_reviews(cls):
        return [review for review in cls.REVIEW_LIST]

    # ----------------------------------------------------------------------------------
    # return  the customer that gave that specific reveiw
    @property
    def customer_name(self):
        return self._customer

    # ----------------------------------------------------------------------------------
    # return the restaurant that this review belongs to
    @property
    def restaurant(self):
        return self._restaurant


# print(review1.rating)
# print(review2.rating)
# print(review3.rating)