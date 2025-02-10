import random

sum = 0
DiceRoll = (int(input("Enter Dice Roll: ")))
for i in range(1, DiceRoll+1):
    roll = random.randint(1,6)
    print(roll)
    sum = sum +roll
print("The sum of all the dices are " + str(sum))