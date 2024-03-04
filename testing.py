import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card[0] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card[0] == 'Ace':
            num_aces += 1
        else:
            value += int(card[0])
    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    return value

def main():
    deck = create_deck()
    shuffle_deck(deck)
    
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    print("Player's hand:", player_hand)
    print("Dealer's hand:", [dealer_hand[0], 'Hidden'])
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    # Player's turn
    while player_value < 21:
        decision = input("Do you want to hit or stand? ").lower()
        if decision == 'hit':
            player_hand.append(deal_card(deck))
            print("Player's hand:", player_hand)
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print("Player busts! Dealer wins.")
                return
        elif decision == 'stand':
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")
    
    # Dealer's turn
    print("Dealer's hand:", dealer_hand)
    while dealer_value < 17:
        dealer_hand.append(deal_card(deck))
        print("Dealer's hand:", dealer_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        if dealer_value > 21:
            print("Dealer busts! Player wins.")
            return
    
    # Determine the winner
    if player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
   while 1 > 0:
        main()
