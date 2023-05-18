from random import choice

random_symbols = [4, 5, 8, 16, 333, 28, 11, 95, 161, 90, 'b', 'p', 'a', 'z', 'v']
first_up = choice(random_symbols)
twice_up = choice(random_symbols)
third_up = choice(random_symbols)
forth_up = choice(random_symbols)
fivs_up = choice(random_symbols)

print(f'Билет с комбинацией чисел и цифр - {first_up} {twice_up} {third_up} {forth_up} {fivs_up} является выигрышным.')