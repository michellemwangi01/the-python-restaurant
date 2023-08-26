from customer import Customer
from restaurant import Restaurant
from review import Review

# -------------------------------------------------------------------
customer1 = Customer("Mirah","Samirah")
customer2 = Customer("Samantha","Mariah")
customer3 = Customer("John","Doe")

# -------------------------------------------------------------------
restaurant1 = Restaurant("Hibbs")
restaurant2 = Restaurant("Naivas")
restaurant3 = Restaurant("Quickmart")

# -------------------------------------------------------------------
review1 = Review(customer1, restaurant1, 10)
review2 = Review(customer2, restaurant1, 12)
review3 = Review(customer3, restaurant2, 13)
review4 = Review(customer3, restaurant2, 13)
review5 = Review(customer2, restaurant2, 1)
review6 = Review(customer2, restaurant2, 18)

# -------------------------------------------------------------------
restaurant1.add_review([review1, review2])
restaurant2.add_review([review3, review4, review5, review6])

# -------------------------------------------------------------------
# print(restaurant2.restaurant_reviews)
# print(restaurant2.customers_with_reviews())
print(customer2.add_reviewed_restaurants())