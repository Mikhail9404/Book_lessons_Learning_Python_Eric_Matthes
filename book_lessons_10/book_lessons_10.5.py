filename = 'answer_programmist.txt'
name = input("Здравствуйте! \nСкажите, почему Вам нравится программировать?"
             "\nДля выхода введите 'q':  ")

while name != 'q':
    with open(filename, 'a') as file_object:
        file_object.write(f"{name}\n")
    name = input("Здравствуйте! \nСкажите, почему Вам нравится программировать?"
             "\nДля выхода введите 'q':  ")


print("Спасибо за Ваш ответ!")



