name = input("Здравствуйте! \nВведите, пожалуйста, Ваше имя: ")

filename = 'guest.txt'
with open(filename, 'a') as file_object:
    file_object.write(f"{name}\n")