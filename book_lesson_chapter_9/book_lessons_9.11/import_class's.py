from classes import User, Admin, Privileges

user_admin = Admin('mikhail', 'kuznetsov', 'russia', '04.04.1994')
user_admin.privileges.show_privileges()