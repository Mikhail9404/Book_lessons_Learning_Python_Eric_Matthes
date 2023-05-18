# Зациклинная программа!!!!!!!!!!!!!!!!!!!

promt = "Введите, пожалуйста, топпинг для Вашей пиццы! "
topping = input(promt)

while True:


    if topping != 'quit':
        print(f"{topping.title()} добавлен(а) в Вашу пиццу!")
    else:
        print("Спасибо, Ваш заказ составлен!")
