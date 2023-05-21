import json

def get_favorite_number():
    """Получает любимое число из файла, если оно существует"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def favorite_number():
    """Проверяет наличие файла и записанного числа, если число уже было записано - сообащает его, нет - записывает"""
    favorite_number = get_favorite_number()
    if favorite_number:
        print(f"Я знаю Ваше любимое число! Это {favorite_number}!")
    else:
        favorite_number = input(f"Введите, пожалуйста, Ваше любимое число: ")
        filename = 'favorite_number.json'
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
            print(f"Я запомнил Ваше любимое число - {favorite_number}!")


favorite_number()


