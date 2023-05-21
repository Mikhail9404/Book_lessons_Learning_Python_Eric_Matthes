sandwich_orders = ['gamburger', 'Panini', 'Krock-madam', 'Ruben', 'BLT', 'Dagwud']
finished_sandwiches = []

while sandwich_orders:
    coock_sandwich = sandwich_orders.pop()  # Поочередное удаление сэндвичей

    print(f'Я готовлю сэндвич - {coock_sandwich}')
    finished_sandwiches.append(coock_sandwich)

print(f'\nСэндвичи приготовлены! \nСписок сэндвичей:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)