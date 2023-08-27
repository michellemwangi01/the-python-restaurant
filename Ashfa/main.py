from restaurant import Restaurant
from review import Review
from customer import Customer

customer1 = Customer("Allan", "Kunta")
customer2 = Customer("Camila", "Carlos")
customer3 = Customer("Abdi", "Jalwo")

# print("Customers:", [customer.full_name() for customer in Customer.all()])
# print(customer1.given_name)
# print(customer1.full_name)
# lists = Customer.all()
# for i in lists:
#     print(i)
# print(customer1.restaurants_reviewed())


# --------------------------------------------------------
restaurant1 = Restaurant("Alabasta")
restaurant2 = Restaurant("Konoha")
restaurant3 = Restaurant("Sky_land")
restaurant4 = Restaurant("Horizon")
restaurant5 = Restaurant("Marita")
# print(restaurant1._name)
# print(Review.review1.rating)
# --------------------------------------------------------

review4 = Review(customer1, restaurant1, 9)
review2 = Review(customer1, restaurant4, 2)
review1 = Review(customer2, restaurant2, 1)
review3 = Review(customer3, restaurant2, 7)
review5 = Review(customer2, restaurant5, 5)
review5 = Review(customer2, restaurant2, 5)
all_reviews = Review.print_all_reviews()
print(Customer.review_list)
Customer.get_rev(all_reviews)
# print(review1.restaurant)


# ------------------- RESTAURANT REVIEWS -------------------------------------
# return all the restaurant reviews
# print(restaurant2.get_restuarant_reveiw())
# -------------------- RESTUARANT UNIQUE CUSTOMERS ---------------------------
# print(len(restaurant1.get_customer_that_gave_the_restaurant_review()))
# print((restaurant1.get_customer_that_gave_the_restaurant_review()))




"""
[
    {'first_name': 'Allan', 'family_name': 'Kunta', 'restaurant_name': 'Alabasta', 'rating': 4},
    {'first_name': 'Allan', 'family_name': 'Kunta', 'restaurant_name': 'Konoha', 'rating': 2}, 
    {'first_name': 'Allan', 'family_name': 'Kunta', 'restaurant_name': 'Sky_land', 'rating': 5}

]
"""

