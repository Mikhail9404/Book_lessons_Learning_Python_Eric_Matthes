message = "Введите, пожалуйста, Ваш возраст! "
message += "\nДля выхода наберите 'quit': "

while True:
    age = input(message)
    age1 = int(age)

    if age == 'quit':
        break
    elif age1 < 3:
        print(f"Билет для поситителей {age} лет бесплатный!")
    elif age1 < 12:
        print(f"Билет для поситителей {age} лет стоит 10$!")
    else:
        print(f"Билет для поситителей {age} лет стоит 15$!")
    break