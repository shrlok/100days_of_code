############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  random_card = random.choice(cards)
  return int(random_card)

def card_sum(cards):
    sum = 0
    for i in cards:
        sum += i
    return sum

def hit():
    player_cards.append(deal_card())
    if card_sum(dealer_cards) < 16:
        dealer_cards.append(deal_card())

def final_result():
    print(f"    Your score: {card_sum(player_cards)}")
    print(f"    Computer's score {card_sum(dealer_cards)}" )
def result():
    print(f"    Your cards: {player_cards}, current score: {card_sum(player_cards)}")
    print(f"    Computer's first card: {dealer_cards[0]}")




player_cards = [deal_card(), deal_card()]
dealer_cards = [deal_card(), deal_card()]
game_over = False
player_win = False
player_lose = False
deal = False

while not game_over:

    #black jack chrck
    if card_sum(player_cards) == 21 and card_sum(dealer_cards) == 21:
        deal = True
    if card_sum(player_cards) == 21:
            player_win = True
    elif card_sum(dealer_cards) == 21:
        player_lose = True


    #ACE check
    elif 11 in player_cards and card_sum(player_cards) > 21:
        player_cards[player_cards.index(11)] = 1
    #over score chrck
    elif card_sum(player_cards) > 21:
        player_lose = True

    else:
        result()
        get_card = input("Type 'y' to get another card, type 'n' to pass:")

        if get_card == "y":
            hit()
        else:
            if card_sum(player_cards) > card_sum(dealer_cards):
                player_win = True
            elif card_sum(player_cards) == card_sum(dealer_cards):
                deal = True
            else:
                player_lose = True
            game_over = True


    if player_win:
        final_result()
        print("You Win!")
        game_over = True
    if player_lose:
        final_result()
        print("Dealer Win!")
        game_over = True
    if deal:
        final_result()
        print("Deal")
        game_over = True