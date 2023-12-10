### Phase-3-SQLAlchemy-Code-Challenge-Restaurants

## AUTHOR
** Ian Mwenda **

## DESCRIPTION
In this code challenge, we'll be working with a restaurant review domain, implementing SQLAlchemy migrations, relationships, and querying. The project involves three models: Restaurant, Review, and Customer. A Restaurant has many Reviews, a Customer has many Reviews, and a Review belongs to both a Restaurant and a Customer. The relationship between Restaurant and Customer is a many-to-many relationship.

## INSTRUCTIONS
Build the methods listed in the deliverables section. Though the suggested order is provided, feel free to tackle the methods in an order you find appropriate. Some methods depend on others, so be cautious.

Note: This code challenge does not include tests, so running pytest won't work. You need to create your own sample instances and test your code in the console.

Create sample data using the seeds.py file to test your models and relationships. Prioritize writing methods that work and test your code in the console.

## SETTING UP
1. Migrations and Models: Create migrations for the initial Restaurant and Customer models. Seed data for some Restaurants and Customers.

2.  Reviews Table: Create a migration for the reviews table with the necessary columns, including star_rating.

3.    Sample Data: Use the seeds.py file to create instances of all your classes for testing.

## Object Relationship Methods
# Review

    Review customer(): Returns the Customer instance for this review.
    Review restaurant(): Returns the Restaurant instance for this review.

# Restaurant

    Restaurant reviews(): Returns a collection of all the reviews for the Restaurant.
    Restaurant customers(): Returns a collection of all the customers who reviewed the Restaurant.

# Customer

    Customer reviews(): Returns a collection of all the reviews that the Customer has left.
    Customer restaurants(): Returns a collection of all the restaurants that the Customer has reviewed.

## Aggregate and Relationship Methods
# Customer

    Customer full_name(): Returns the full name of the customer, with the first name and last name concatenated, Western style.
    Customer favorite_restaurant(): Returns the restaurant instance with the highest star rating from this customer.
    Customer add_review(restaurant, rating): Creates a new review for the restaurant with the given restaurant_id.
    Customer delete_reviews(restaurant): Removes all reviews for this restaurant.

# Review

    Review full_review(): Returns a string formatted as follows: "Review for {restaurant name} by {customer's full name}: {review star_rating} stars."

# Restaurant

    Restaurant fanciest(): Returns one restaurant instance for the restaurant with the highest price.
    Restaurant all_reviews(): Returns a list of strings with all the reviews for this restaurant formatted as specified.

## TECHNOLOGIES
- PYTHON

## Support and contact details

- email :: ianmwenda@gmail.com
- phone :: +25422222222

## License

*Licenced under the MIT Licence Copyright (c) 2023 **Ian Mwenda M
