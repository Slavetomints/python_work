from restaurant import Restaurant


class IceCreamShop(Restaurant):
    """Represents an ice cream shop"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of parent class, then 
        initialize attributes specific to an ice cream shop
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'blue moon']

    def display_flavors(self):
        """Displays the flavors an ice cream stand has"""
        print(f'{self.restaurant_name} has these flavors:')
        for flavor in self.flavors:
            print(f'\n-{flavor.title()}')

dairy_haus = IceCreamShop('Dairy Haus', 'Desert')
dairy_haus.display_flavors()