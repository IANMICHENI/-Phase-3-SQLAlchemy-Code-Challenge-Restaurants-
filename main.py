from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Create the database engine
engine = create_engine('sqlite:///restaurant_reviews.db')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def main():
    # Display all customers
    all_customers = session.query(Customer).all()
    print("All Customers:")
    for customer in all_customers:
        print(f"{customer.first_name} {customer.last_name}")

    # Display all restaurants
    all_restaurants = session.query(Restaurant).all()
    print("\nAll Restaurants:")
    for restaurant in all_restaurants:
        print(f"{restaurant.name} - Price: {restaurant.price}")

    # Display all reviews
    all_reviews = session.query(Review).all()
    print("\nAll Reviews:")
    for review in all_reviews:
        print(f"Review for {review.restaurant.name} by {review.customer.full_name()}: {review.star_rating} stars")

if __name__ == "__main__":
    main()
