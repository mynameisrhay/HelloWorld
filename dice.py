# 15th exercise. create a Dice (class) which has a roll function. every time the dice rolls, it must generate a
# random tuple between 1 and 6.
import random


class Dice:
    def roll(self):
        dice_val1 = random.randint(1, 6)
        dice_val2 = random.randint(1, 6)
        return dice_val1, dice_val2


dice1 = Dice()
print(dice1.roll())
