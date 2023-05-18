class Restuarant():
    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
        print(f"Hello, visitor! {self.restuarant_name} with type - {self.cuisine_type} welcome to you!")

    def open_restuarant(self):
        print(f"Restuarant {self.restuarant_name} is open.")

restuarant = Restuarant('"Vkusno i Tochka"', 'Russia')

print(restuarant.restuarant_name)
print(restuarant.cuisine_type)

restuarant.describe_restuarant()
restuarant.open_restuarant()