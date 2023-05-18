class Restuarant():
    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
        print(f"Hello, visitor! {self.restuarant_name} with type - {self.cuisine_type} welcome to you!")

    def open_restuarant(self):
        print(f"Restuarant {self.restuarant_name} is open.")

resturant_1 = Restuarant('Frank', 'Grill bar')
resturant_2 = Restuarant('KFC', 'Fast food')
resturant_3 = Restuarant('Tokio', 'Asia food')

resturant_1.describe_restuarant()
resturant_2.describe_restuarant()
resturant_3.describe_restuarant()