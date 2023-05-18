promt = "Введите, пожалуйста, топпинг для Вашей пиццы! "

while True:
    topping = input(promt)

    if topping != 'quit':
        print(f"{topping.title()} добавлен(а) в Вашу пиццу!")
    else:
        break