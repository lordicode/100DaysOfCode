#using System Random for a more random result, avoiding using simple Marsenne Twister for more or less
import random

foo = random.SystemRandom()

signs = ["Gun", "Lightning", "Devil", "Dragon", "Water", "Air", "Paper", "Sponge", "Wolf", "Tree", "Human", "Snake",
         "Scissors", "Fire", "Rock"]

your_sign = input("What is your play here?\nGun, Lightning, Devil, Dragon, Water, Air, Paper, Sponge, Wolf, Tree, Human, Snake, Scissors, Fire, Rock?\nEnter a number from 0 to 14->")
your_sign = int(your_sign)
sign_index = foo.randint(0, len(signs) - 1)
os_sign = signs[sign_index]
print("Your OS plays: ", os_sign, sign_index)
if sign_index - your_sign == 1:
    print()
elif sign_index - your_sign == -1:
    print()

