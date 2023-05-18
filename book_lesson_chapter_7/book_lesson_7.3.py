number = input('Назовите число и программа скажет, четное оно или нет: ')
number = int(number)

if number % 2 == 0:
    print(f"Число {number} четное!")
else:
    print(f"Число {number} нечетное!")