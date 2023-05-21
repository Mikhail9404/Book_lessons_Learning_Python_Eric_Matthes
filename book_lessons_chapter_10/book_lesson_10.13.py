import json

def get_stored_username():
    """Полуает хранимое имя пользователя, если оно существует."""
    filename = '../book_lessons_part_6/book_lessons_10/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input(f"Введите, пожалуйста, Ваше имя: ")
    filename = '../book_lessons_part_6/book_lessons_10/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"Я Вас запомнил, возвращайтесь позже, {username}!")
    return username

def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Добро пожаловать, {username}!")
    else:
        username = get_new_username()

def check_name():
    username = get_stored_username()
    if username:
        check = input(f"Здравствуйте, Ваше имя {username}? Ответьте, пожалуйста, 'yes'/'no': ")
        if check == 'yes':
            greet_user()
        elif check == 'no':
            get_new_username()
        else:
            print("Ввод некорректный!")

check_name()