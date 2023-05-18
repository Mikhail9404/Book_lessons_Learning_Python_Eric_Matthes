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


class Admin(User):
    def __init__(self, first_name, last_name, country, birthday_date):
        super().__init__(first_name, last_name, country, birthday_date)
        self.privileges = ['allowed to add messages', 'allowed to delete users', 'allowed to ban users']

    def show_privileges(self):
        print(f"Admin has privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")

user_admin = Admin('mikhail', 'kuznetsov', 'russia', '04.04.1994')
user_admin.show_privileges()