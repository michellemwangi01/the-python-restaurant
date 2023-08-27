from customer import Customer
from restaurant import Restaurant
from review import Review

print("\n------------------------------------- CUSTOMERS ------------------------------------------")
customer1 = Customer("Mirah","Samirah")
customer2 = Customer("Samantha","Mariah")
customer3 = Customer("John","Doe")
customer4 = Customer("John","Smith")
print(customer4.full_name)
print(customer3.full_name)
print(customer2.full_name)
print(customer1.full_name)


print("\n----------------------------------- RESTAURANTS ------------------------------------------")
restaurant1 = Restaurant("Hibbs")
restaurant2 = Restaurant("Naivas")
restaurant3 = Restaurant("Quickmart")
print(restaurant3.name)
print(restaurant2.name)
print(restaurant1.name)


print("\n--------------------------------- REVIEWS ------------------------------------------------")
review1 = Review(customer1, restaurant1, 10)
review2 = Review(customer2, restaurant1, 12)
review3 = Review(customer3, restaurant2, 13)
review4 = Review(customer3, restaurant2, 13)
review5 = Review(customer2, restaurant2, 1)
review6 = Review(customer2, restaurant2, 18)
print(f'List of reviews({len(Review.REVIEWS)}): \n {Review.REVIEWS}')



print("\n-------------------------------restaurant add_review()----------------------------------")
restaurant1.add_review([review1, review2])
restaurant2.add_review([review3, review4, review5, review6])
print(f"List of '{restaurant1.name}' reviews({len(restaurant1.restaurant_reviews)}): \n {restaurant1.restaurant_reviews}")


print("\n-------------------------------customer add_review()-------------------------------------")
customer1.add_review(restaurant3, 23)
print(f"Reviews by {customer1.full_name}:\n {customer1.reviews()}")

print("\n-------------------------------restaurant restaurant_reviews()---------------------------")
print(f"{restaurant2.name}'s reviews:\n{restaurant2.restaurant_reviews}")

print("\n-------------------------------restaurant customers reviews------------------------------")
print(restaurant2.customers_with_reviews())

print("\n------------------------------- customer reviews-----------------------------------------")
print(customer3.reviewed_restaurants)

print("\n------------------------------- find_customer_by_full_name ------------------------------")
print(Customer.find_customer_by_full_name('john doe'))

print("\n------------------------------- find_customer_by_given_name -----------------------------")
print(Customer.find_customer_by_given_name('john'))

print("\n------------------------------- average_star_rating ------------------------------------")
print(restaurant2.average_star_rating())
