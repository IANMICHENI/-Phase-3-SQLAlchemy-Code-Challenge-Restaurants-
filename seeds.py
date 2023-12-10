# seeds.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Data seeding (creating sample data)
restaurant1 = Restaurant(name="CJ's", price=490)
restaurant2 = Restaurant(name="Kilimanjaro", price=650)
customer1 = Customer(first_name="Ian", last_name="Mwenda")
customer2 = Customer(first_name="Elvis", last_name="Mawira")

# Create reviews and link them to restaurants and customers
review1 = Review(content="Greate food!", star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(content="Nice food!", star_rating=4, restaurant=restaurant2, customer=customer2)
# Add instances to the session and commit
session.add_all([restaurant1, restaurant2, customer1, review1])
session.commit()