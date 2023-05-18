from class_User import User

class Privileges():
    def __init__(self):
        self.privileges = ['allowed to add messages', 'allowed to delete users', 'allowed to ban users']

    def show_privileges(self):
        print(f"\nAdmin has privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    def __init__(self, first_name, last_name, country, birthday_date):
        super().__init__(first_name, last_name, country, birthday_date)
        self.privileges = Privileges()

