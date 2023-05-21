import class_Privileges_Admin

user_admin = class_Privileges_Admin.Admin('mikhail', 'kuznetsov', 'russia', '04.04.1994')
user_admin.describe_user()
user_admin.privileges.show_privileges()