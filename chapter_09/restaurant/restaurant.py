"""A class that can be used to represent a restaurant"""

class Restaurant:
    """Represents a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to represent a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_of_customers = 0
    
    def describe_restaurant(self):
        """Give info about a restaurant"""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type} food.")
        print(f'The restaurant has served {self.number_of_customers} customer(s)')

    def open_restaurant(self):
        """Display the restaurant is open"""
        print(f'{self.restaurant_name} is now open')

    def set_number_served(self, customers):
        """Allows you to set the number of customers served"""
        self.number_of_customers = customers

    def increment_number_served(self, increment):
        """Allows you to increment the number of customers"""
        self.number_of_customers += increment