# using System Random for a more random result, avoiding using simple Marsenne Twister for more or less
import random
#call module with art
import ascii_art

foo = random.SystemRandom()

signs = ["Tree", "Human", "Snake",
         "Scissors", "Fire", "Rock", "Gun", "Lightning", "Devil", "Dragon", "Water", "Air", "Paper", "Sponge", "Wolf"]

sign_index_player = input(
    "What is your play here?\nGun, Lightning, Devil, Dragon, Water, Air, Paper, Sponge, Wolf, Tree, Human, Snake, "
    "Scissors, Fire, Rock?\nEnter a number from 0 to 14->")
sign_index_player = int(sign_index_player)
#quit with assert error if invalid input
assert 14 >= sign_index_player >= 0
#get ransom number from range
sign_index_os = foo.randint(0, len(signs) - 1)
os_sign = signs[sign_index_os]
player_sign = signs[sign_index_player]

print(f"Computer has chosen: {os_sign}, {sign_index_os}\n", ascii_art.ascii_sign(sign_index_os))
print(f"\nYou have chosen: {player_sign}, {sign_index_player}\n", ascii_art.ascii_sign(sign_index_player))

if sign_index_os == sign_index_player:
    print("It is a draw!\n")
elif sign_index_player == 0 and sign_index_os <= 7:
    print("You won!")
elif sign_index_player == 1 and (14 > sign_index_os >= 9 or sign_index_os == 0):
    print("You won!")
elif sign_index_player == 2 and (10 <= sign_index_os <= 14 or sign_index_os <= 1):
    print("You won!")
elif sign_index_player == 3 and (11 <= sign_index_os <= 14 or sign_index_os <= 2):
    print("You won!")
elif sign_index_player == 4 and (12 <= sign_index_os <= 14 or sign_index_os <= 3):
    print("You won!")
elif sign_index_player == 5 and ((sign_index_os == 14 or sign_index_os == 13) or (sign_index_os < sign_index_player)):
    print("You won!")
elif sign_index_player == 6 and (0 <= sign_index_os < sign_index_player or sign_index_os == 14):
    print("You won!")
elif sign_index_player == 7 and sign_index_os < sign_index_player:
    print("You won!")
elif sign_index_player == 8 and (1 <= sign_index_os <= 7):
    print("You won!")
elif sign_index_player == 9 and (2 <= sign_index_os <= 8):
    print("You won!")
elif sign_index_player == 10 and (3 <= sign_index_os <= 9):
    print("You won!")
elif sign_index_player == 11 and (4 <= sign_index_os <= 10):
    print("You won!")
elif sign_index_player == 12 and (5 <= sign_index_os <= 11):
    print("You won!")
elif sign_index_player == 13 and (6 <= sign_index_os <= 12):
    print("You won!")
elif sign_index_player == 14 and (7 <= sign_index_os <= 13 or sign_index_os == 0):
    print("You won!")
else:
    print("PC won!")
