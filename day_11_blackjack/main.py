# Blackjack Project

# The House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from art import logo
from random import choice
# from replit import clear


def wipe():  # replit clear doesn't really work well if you run outside their environment, so using this trick instead
    print('\n'*100)


def blackjack():
    player_hand = [deal(), deal()]
    dealer_hand = [deal(), deal()]

    keep_playing = True

    while keep_playing:
        print(f'    Your cards: {player_hand}, current score: {calc_hand(player_hand)}')
        print(f'    Dealer\'s first card: {dealer_hand[0]}')
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_hand.append(deal())
            if calc_hand(player_hand) > 21:
                keep_playing = False
            elif calc_hand(player_hand) == 0:
                keep_playing = False
        else:
            keep_playing = False
    if calc_hand(player_hand) < 22:
        calc_dealer_score(dealer_hand)
    reveal(player_hand, dealer_hand)
    play_game()


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def reveal(player_hand, dealer_hand):
    print(f'    Your final hand: {player_hand}, final score: {calc_hand(player_hand)}')
    print(f'    Dealer\'s final hand: {dealer_hand}, final score: {calc_hand(dealer_hand)}')
    if calc_hand(player_hand) > 21:
        print("You went over! You lost.")
    elif calc_hand(player_hand) == 0:
        print("You got Blackjack! You won.")
    elif calc_hand(dealer_hand) > 21:
        print("The dealer busted! You won.")
    elif calc_hand(player_hand) == calc_hand(dealer_hand):
        print("You had a draw! No winner.")
    elif calc_hand(player_hand) < calc_hand(dealer_hand):
        print("The dealer had a higher hand! You lost.")
    elif calc_hand(player_hand) > calc_hand(dealer_hand):
        print("Your hand beat the dealer\'s! You won.")

        # Note: not needed, but can add better condition handling of blackjacks


def calc_dealer_score(dealer_hand):
    while calc_hand(dealer_hand) < 17:
        dealer_hand.append(deal())
        calc_dealer_score(dealer_hand)


def play_game():
    if input("Do you want to play a game of Blackjack? type 'y' or 'n': ") == 'y':
        # clear()
        wipe()
        print(logo)
        blackjack()
    else:
        print('Thanks for playing. Come back soon.')


def calc_hand(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        return sum(hand)
    else:
        return sum(hand)


play_game()
