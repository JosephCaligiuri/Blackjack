import random
import time
import os

# Initialize colorama
import colorama
colorama.init()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define the card ranks, suits, and values
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Function to create a deck of cards
def create_deck(num_decks=6):
    deck = []
    for _ in range(num_decks):
        for suit in suits:
            for rank in ranks:
                deck.append((rank, suit))
    random.shuffle(deck)
    return deck

# Function to calculate the total value of a hand
def calculate_total(hand):
    total = sum(values[card[0]] for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

# Function to display a card
def display_card(card):
    rank, suit = card
    print(colorama.Fore.RED if suit in ['Hearts', 'Diamonds'] else colorama.Fore.BLACK, end="")
    print(f" {rank} of {suit}", end="")
    print(colorama.Style.RESET_ALL, end="")

# Function to display a hand
def display_hand(hand, hide_first_card=False):
    for i, card in enumerate(hand):
        if i == 0 and hide_first_card:
            print("Hidden Card", end="")
        else:
            display_card(card)
        if i < len(hand) - 1:
            print(",", end=" ")
    print()

# Function to handle player's turn
def player_turn(deck, player_hand, dealer_hand):
    while True:
        clear_screen()
        print("Dealer's Hand:")
        print("Hidden Card, ", end="")
        display_card(dealer_hand[1])
        print()
        print("\nYour Hand:")
        display_hand(player_hand)
        print("\nTotal:", calculate_total(player_hand))
        print("\n1 - Hit")
        print("2 - Stand")
        print("3 - Double Down")
        print("4 - Split (if you have a pair)")
        choice = input("Choose your action: ")
        if choice == '1':
            player_hand.append(deck.pop())
            total = calculate_total(player_hand)
            if total > 21:
                return 'bust'
        elif choice == '2':
            return 'stand'
        elif choice == '3':
            if len(player_hand) == 2:  # Can only double down on the first two cards
                player_hand.append(deck.pop())
                return 'double'
            else:
                print("You can only double down on the first two cards!")
                time.sleep(2)
        elif choice == '4':
            if len(player_hand) == 2 and player_hand[0][0] == player_hand[1][0]:  # Check if it's a pair
                return 'split'
            else:
                print("You can only split if you have a pair!")
                time.sleep(2)
        else:
            print("Invalid choice! Please choose again.")

# Function to handle dealer's turn
def dealer_turn(deck, dealer_hand):
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

# Function to determine the winner
def determine_winner(player_hand, dealer_hand):
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    if player_total > 21:
        return 'dealer'
    elif dealer_total > 21:
        return 'player'
    elif player_total > dealer_total:
        return 'player'
    elif player_total < dealer_total:
        return 'dealer'
    else:
        return 'push'

# Main game loop
def play_game():
    deck = create_deck()
    while len(deck) > 20:  # Make sure there are enough cards in the shoe
        clear_screen()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        if calculate_total(player_hand) == 21:
            print("Blackjack! You win!")
            time.sleep(2)
            continue
        while True:
            action = player_turn(deck, player_hand, dealer_hand)
            if action == 'bust':
                print("Bust! You lose!")
                time.sleep(2)
                break
            elif action == 'stand':
                dealer_turn(deck, dealer_hand)
                winner = determine_winner(player_hand, dealer_hand)
                if winner == 'player':
                    print("You win!")
                elif winner == 'dealer':
                    print("Dealer wins!")
                else:
                    print("It's a push!")
                time.sleep(2)
                break
            elif action == 'double':
                dealer_turn(deck, dealer_hand)
                winner = determine_winner(player_hand, dealer_hand)
                if winner == 'player':
                    print("You win!")
                elif winner == 'dealer':
                    print("Dealer wins!")
                else:
                    print("It's a push!")
                time.sleep(2)
                break
            elif action == 'split':
                hand = list(hand)  # Convert tuple to list
        display_hand([hand])
        print("\nTotal:", calculate_total([hand]))
        print("\n1 - Hit")
        print("2 - Stand")
        choice = input("Choose your action: ")
        if choice == '1':
            hand.append(deck.pop())
            total = calculate_total(hand)
            if total > 21:
                print("Bust! You lose this hand!")
                time.sleep(2)
                continue
        elif choice == '2':
            continue
        else:
            print("Invalid choice! Please choose again.")
            time.sleep(2)
        dealer_turn(deck, dealer_hand)
        winner = determine_winner(player_hand[0], dealer_hand)
        if winner == 'player':
            print("You win the first hand!")
        elif winner == 'dealer':
            print("Dealer wins the first hand!")
        else:
            print("It's a push for the first hand!")
        time.sleep(2)
        winner = determine_winner(player_hand[1], dealer_hand)
        if winner == 'player':
            print("You win the second hand!")
        elif winner == 'dealer':
            print("Dealer wins the second hand!")
        else:
            print("It's a push for the second hand!")
        time.sleep(2)
        break
    print("Game over!")

# Play the game
play_game()
