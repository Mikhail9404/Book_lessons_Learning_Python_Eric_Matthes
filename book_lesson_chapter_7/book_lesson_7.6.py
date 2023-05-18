promt = "Введите, пожалуйста, топпинг для Вашей пиццы! "
active = True

while active:
    topping = input(promt)

    if topping != 'quit':
        print(f"{topping.title()} добавлен(а) в Вашу пиццу!")
    else:
        print("Спасибо, Ваш заказ составлен!")
        active = False