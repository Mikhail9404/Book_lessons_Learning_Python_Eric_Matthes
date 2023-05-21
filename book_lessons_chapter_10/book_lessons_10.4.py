filename = 'guest_book.txt'
name = input("Здравствуйте! \nВведите, пожалуйста, Ваше имя!"
             "\nДля выхода введите 'q':  ")

while name != 'q':
    with open(filename, 'a') as file_object:
        file_object.write(f"{name}\n")
    name = input("Здравствуйте! \nВведите, пожалуйста, Ваше имя: "
                 "\nДля выхода введите 'q'! ")


print("Спасибо! Список гостей составлен!")



