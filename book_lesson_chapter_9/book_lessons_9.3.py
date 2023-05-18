class User():
    def __init__(self, first_name, last_name, country, birthday_date):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.country = country.title()
        self.birthday_date = birthday_date

    def describe_user(self):
        print(f"\nFirst name: {self.first_name} \nLast name: {self.last_name} \nCountry: {self.country} \nBirthday date: {self.birthday_date}")

    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name}! Welcome!")


user_1 = User('mikhail', 'kuznetsov', 'russia', '04.04.1994')
user_2 = User('ben', 'aflik', 'amerika', '16.12.1986')
user_3 = User('viktor', 'kedly', 'africa', '28.08.2002')



user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
