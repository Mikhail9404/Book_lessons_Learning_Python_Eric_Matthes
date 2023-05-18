class User():
    def __init__(self, first_name, last_name, country, birthday_date):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.country = country.title()
        self.birthday_date = birthday_date
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nFirst name: {self.first_name} \nLast name: {self.last_name} \nCountry: {self.country}"
              f" \nBirthday date: {self.birthday_date}")

    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name}! Welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User('mikhail', 'kuznetsov', 'russia', '04.04.1994')
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)