from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for i in range(10):
            print(randint(1, self.sides))


#model_roll_1 = Die()
#model_roll_1.roll_die()
#model_roll_2 = Die(10)
#model_roll_2.roll_die()
model_roll_3 = Die(20)
model_roll_3.roll_die()