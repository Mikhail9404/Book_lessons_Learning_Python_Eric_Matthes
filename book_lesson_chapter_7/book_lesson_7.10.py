responses = {}

polling_active = True

while polling_active:
    name = input(f"Как Вас зовут? ")
    resort = input(f"Где бы Вы хотели провести отпуск? ")

    responses[name] = resort

    repeat = input(f"Хотели бы Вы продолжить опрос других людей? (Да/Нет) ")
    if repeat == ("Нет" or "нет"):
        polling_active = False



print("\n---   Итоги опроса ---")
for name, resort in responses.items():
    print(f"{name} хочет провести опуск в(на) {resort}")