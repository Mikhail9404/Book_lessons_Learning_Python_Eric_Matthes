def make_sandwitch(bread, souce, *toppings):
    if toppings:
        print(f"\nСендвич на {bread} хлебе с соусом {souce} и топпингами: ")
        for topping in toppings:
            print(f"- {topping}")
    else:
        print(f"\nСендвич на {bread} хлебе с соусом {souce} без топпингов.")

make_sandwitch('белом', 'сырный', 'бекон', 'сладкий лук', 'двойной сыр')
make_sandwitch('белом с пармизаном', 'карри')
make_sandwitch('белом', 'сырный', 'сладкий лук')