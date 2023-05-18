from random import choice

random_symbols = [4, 5, 8, 16, 333, 28, 11, 95, 161, 90, 'b', 'p', 'a', 'z', 'v']
result = []
my_result = ['z', '90', '95', 'v', '161']
quantity = 0


while my_result != result:
    result = []
    for i in range(5):
        result.append(str(choice(random_symbols)))
    quantity += 1


print(f'Количество попыток - {quantity}')
print(result)
print(my_result)
