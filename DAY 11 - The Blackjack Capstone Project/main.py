from playsound import playsound
import ascii_art
import secrets

def play_bgm():
    playsound(".//BGM.mp3")

played_cards = []

def deal_card(num_cards):
    cards = []
    for i in range(0, num_cards):
        low = 0
        high = 52
        out = secrets.randbelow(high - low) + low  # out = random number from range [low, high)
        if out in played_cards:
            deal_card()
        else:
            cards.append(ascii_art.CARDS[out])
    return cards

def black_jack():
    print("")

#play_bgm()
print(ascii_art.blackjack)
dealer_hand = deal_card(2)
player_1_hand = deal_card(2)

print(dealer_hand[0])
print(dealer_hand[1])
print(player_1_hand[0])
print(player_1_hand[1])