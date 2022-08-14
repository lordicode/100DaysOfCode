import secrets
from time import sleep

from playsound import playsound

import ascii_art


# This function plays background music while the game is ongoing
def play_bgm():
    playsound(".//BGM.mp3", False)


# this keeps track of all the cards that were dealt this game
played_cards = []


# main function that takes a number of cards to be dealt
# and returns a list with all the cards
def deal_card(num_cards):
    cards = []
    for i in range(0, num_cards):
        low = 0
        high = 52
        # the python module Secrets allows for cryptographically secure number generation
        out = secrets.randbelow(high - low) + low  # out = random number from range [low, high)
        if out in played_cards:
            # if the cards was already dealt, take another one
            deal_card(1)
        else:
            # if the card wasn't dealt, add it to the draw list
            cards.append(ascii_art.CARDS[out])
    # return a list of how many cards was specified
    return cards


def black_jack():
    summ_cards = 0
    print("Current value of your cards is: ")
    for i in range(0, len(stats[1]['cards'])):
        card = ascii_art.CARDS.index(stats[1]['cards'][i])
        # aces
        if card < 4 and summ_cards + card <= 21:
            summ_cards += 11
        elif card < 4 and summ_cards + card > 21:
            summ_cards += 1
        # kings, queens, valets, and 10s
        elif card < 20:
            summ_cards += 10
        # 9
        elif card < 24:
            summ_cards += 9
        # 8
        elif card < 28:
            summ_cards += 8
        # 7
        elif card < 32:
            summ_cards += 7
        # 6
        elif card < 36:
            summ_cards += 6
        # 5
        elif card < 40:
            summ_cards += 5
        # 4
        elif card < 44:
            summ_cards += 4
        # 3
        elif card < 48:
            summ_cards += 3
        # 2
        else:
            summ_cards += 2
    print(summ_cards)
    sleep(1)
    if summ_cards == 21:
        print("BLACKJACK!")
    elif summ_cards > 21:
        print("OVER!")
    else:
        next_card = input("What do you want to do? Hit or stay?")
        if next_card.lower().strip() == "hit":
            new_card = deal_card(1)
            stats[1]['cards'].append(new_card)
            black_jack()
            # @TODO: logic of revealing dealer's cards and of checking for the score and game ending: over, 21,
            #  under. comparison with dealer
        else:
            print("")
            # @TODO: logic of revealing dealer's cards and of game ending


stats = [{'name': '',
          'cards': []}, {'name': '',
                         'cards': []}]

print("Welcome to the game of Blackjack!")
sleep(1)
# displays the blackjack ascii art
print(ascii_art.blackjack)
sleep(1)
play_bgm()

name = input("Please enter your name? ")
stats[1]['name'] = name
print("Game started!")
sleep(1)
stats[0]['name'] = 'Dealer'
print("Dealer gets 2 cards: ")
sleep(1)
dealer_hand = deal_card(2)
stats[0]['cards'] = dealer_hand
print(ascii_art.hidden_card, dealer_hand[1])

print("You get 2 cards: ")
sleep(1)
player_1_hand = deal_card(2)
stats[1]['cards'] = player_1_hand
print(player_1_hand[0], player_1_hand[1])

# enter main game loop
black_jack()
