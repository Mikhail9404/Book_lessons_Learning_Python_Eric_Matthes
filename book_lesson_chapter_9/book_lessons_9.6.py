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

class IceCreamStand(Restuarant):
    def __int__(self, restuarant_name, cuisine_type):
        super().__init__(restuarant_name, cuisine_type)

    def present_flavors(self):
        self.flavors = ['ice cream', 'cream', 'milk', 'creme brulee', 'sherbet', 'soft (sofuto-kurimu)', 'fruit ice',
                        'gourmet', 'popsicle']
        print(f"Available flavors are: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

my_ice_restuarant = IceCreamStand('baskin robbins', 'ice cream stand')
my_ice_restuarant.describe_restuarant()
my_ice_restuarant.present_flavors()