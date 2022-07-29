#using System Random for a more random result, avoiding using simple Marsenne Twister for more or less
import random
import ascii_art

foo = random.SystemRandom()

signs = ["Gun", "Lightning", "Devil", "Dragon", "Water", "Air", "Paper", "Sponge", "Wolf", "Tree", "Human", "Snake",
         "Scissors", "Fire", "Rock"]

sign_index_player = input("What is your play here?\nGun, Lightning, Devil, Dragon, Water, Air, Paper, Sponge, Wolf, Tree, Human, Snake, Scissors, Fire, Rock?\nEnter a number from 0 to 14->")
sign_index_player = int(sign_index_player)
sign_index_os = foo.randint(0, len(signs) - 1)
os_sign = signs[sign_index_os]
player_sign = signs[sign_index_player]

print(f"Computer has chosen: {os_sign}, {sign_index_os}\n", ascii_art.ascii_sign(sign_index_os))
print(f"\nYou have chosen: {player_sign}, {sign_index_player}\n", ascii_art.ascii_sign(sign_index_player))

if sign_index_os == sign_index_player:
    print("It is a draw! Go again!\n")
elif sign_index_os - sign_index_player > 5:
    print("You lost!\n")
else:
    print("You won!\n")
"""
if index is 0 and enemy is 14, then 0 win
if index of enemy sign is 6 higher than of yours, yours win, else enemy win
if get to the end of list go -1....
so your is 3 - dragon, it beats 2, 1, 0, 14, 13, 12, 11. It is beaten by 4, 5, 6, 7, 8, 9, 10"""

