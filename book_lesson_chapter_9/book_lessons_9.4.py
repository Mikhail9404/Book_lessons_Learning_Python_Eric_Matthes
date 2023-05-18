class Restuarant():
    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_serv = 0

    def describe_restuarant(self):
        print(f"Hello, visitor! {self.restuarant_name} with type - {self.cuisine_type} welcome to you!")

    def open_restuarant(self):
        print(f"Restuarant {self.restuarant_name} is open.")

    def set_number_served(self, visitors):
        self.number_serv = visitors
        print(f"Count visitors for now - {self.number_serv}.")

    def increment_number_served(self, count_visitors):
        self.number_serv += count_visitors
        print(f"Count visitors for now - {self.number_serv}.")


my_restaurant = Restuarant('name', 'italian')
my_restaurant.set_number_served(31)
my_restaurant.increment_number_served(102)