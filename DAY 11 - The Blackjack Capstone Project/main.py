import os
import secrets
from time import sleep
from playsound import playsound
import ascii_art

# this keeps track of all the cards that were dealt this game
played_cards = []

# this keeps track of the player and dealer hands
stats = [{'name': '',
          'cards': []},
         {'name': '',
          'cards': []}]


# This function plays background music while the game is ongoing
def play_bgm():
    playsound(".//BGM.mp3", False)


# this function takes the index of the card in player/dealer hand and assigns it value
# returns the combined sum of values
def count_points(player_id):
    summ_cards = 0
    for i in range(0, len(stats[player_id]['cards'])):
        card = ascii_art.CARDS.index(stats[player_id]['cards'][i])
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
    return summ_cards

#because
def dealer_revealed():
    for i in range(0, len(stats[0]['cards'])):
        card = ascii_art.CARDS.index(stats[0]['cards'][i])
        print(ascii_art.CARDS[card])
    points_dealer = count_points(0)
    return points_dealer


def dealer_less_than():
    print("Dealer deals himself another card")
    dealer_new_card = deal_card(1)
    stats[0]['cards'].append(dealer_new_card[0])
    card = stats[0]['cards'][-1]
    print(f"Dealer card is: {card}")


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

def end_blackjack_game():
    summ_points_player = count_points(1)
    summ_points_dealer = count_points(0)
    print(f"Dealer points: {summ_points_dealer}")
    print(f"Player points: {summ_points_player}")
    if (summ_points_dealer < 21 and summ_points_player < 21) and (
            21 - summ_points_player < 21 - summ_points_dealer):
        print(f"Player - {stats[1]['name']} - won!")
    elif (summ_points_dealer < 21 and summ_points_player < 21) and (
            21 - summ_points_player > 21 - summ_points_dealer):
        print("Dealer won!")
    elif summ_points_player == 21 and summ_points_dealer == 21:
        print("Draw! Blackjack!")
    elif summ_points_dealer > 21 and summ_points_player > 21:
        print("Draw! Over!")
    elif summ_points_dealer <= 21 < summ_points_player:
        print("Dealer won!")
    elif summ_points_player == summ_points_dealer:
        print("Draw! Under!")
    elif summ_points_player == 21 and summ_points_dealer != 21:
        print("Player won!")
    over = input("Do you want to start over? yes or no")
    if over.strip().lower() == 'yes':
        # this restarts this script
        os.system("python main.py")
        print("Restarting...")
        exit()

def reveal(points_dealer, points_player):
    print("Dealer cards: ")
    dealer_revealed()
    print("Player cards: ")
    for i in range(0, len(stats[1]['cards'])):
        card = ascii_art.CARDS.index(stats[1]['cards'][i])
        print(ascii_art.CARDS[card])

#this function generates and adds one card to player hand
def hit():
    new_card = deal_card(1)
    stats[1]['cards'].append(new_card[0])
    card = stats[1]['cards'][-1]
    print(f"Player gets dealt a new card: {card}")


def black_jack(end_game):
    if end_game == 0:
        summ_points_player = count_points(1)
        if summ_points_player == 22 and len(stats[1]['cards']) == 2:
            summ_points_player = summ_points_player - 10
        summ_points_dealer = count_points(0)
        print(f"Current value of player cards is {summ_points_player}")
        if summ_points_player == 21:
            if summ_points_dealer != summ_points_player:
                reveal(summ_points_dealer, summ_points_player)
                print("Player won!")
                over = input("Do you want to start over? yes or no")
                if over.strip().lower() == 'yes':
                    # this restarts this script
                    os.system("python main.py")
                    print("Restarting...")
                    exit()
            else:
                reveal(summ_points_dealer, summ_points_player)
                print("Draw! Blackjack!")
                over = input("Do you want to start over? yes or no")
                if over.strip().lower() == 'yes':
                    # this restarts this script
                    os.system("python main.py")
                    print("Restarting...")
                    exit()
        else:
            next_card = input("Do you want another Hit? Yes or no")
            if next_card.lower().strip() == "yes":
                if summ_points_dealer <= 17:
                    dealer_less_than()
                hit()
                black_jack(1)
            else:
                end_blackjack_game()
    elif end_game == 1:
        summ_points_player = count_points(1)
        summ_points_dealer = count_points(0)
        if summ_points_player <= 19:
            if summ_points_dealer <= 17:
                dealer_less_than()
                summ_points_dealer = count_points(0)
            another_hit = input("Do you want another Hit? Yes or no")
            if another_hit.lower().strip() == 'yes':
                hit()
                summ_points_player = count_points(1)
                black_jack(1)
            else:
                if summ_points_dealer <= 17:
                    dealer_less_than()
                    summ_points_dealer = count_points(0)
                reveal(summ_points_dealer, summ_points_player)
                end_blackjack_game()
        else:
            if summ_points_dealer <= 17:
                dealer_less_than()
                summ_points_dealer = count_points(0)
        if summ_points_dealer <= 17:
            dealer_less_than()
            summ_points_dealer = count_points(0)
        summ_points_player = count_points(1)
        reveal(summ_points_dealer, summ_points_player)
        end_blackjack_game()

print("Welcome to the game of Blackjack!")
# displays the blackjack ascii art
print(ascii_art.blackjack)
sleep(1)
# start playing background casino music
play_bgm()
sleep(1)
name = input("Please enter your name? ")
stats[1]['name'] = name.title()
print("Game started!")
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
black_jack(0)
