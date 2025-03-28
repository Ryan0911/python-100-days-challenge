# pylint: disable=C0103, C0114, C0301
from blackjack import BlackJackDealer, BlackJackPlayer
from utils.art import ArtHelper

print(ArtHelper.blackjack())
print('-' * 20)
print("Welcome to the Blackjack game!")
print("You have $3000 to start with.")
print("Let's play!")
print('-' * 20)
dealer = BlackJackDealer(deck = 1)
player = BlackJackPlayer(money = 3000)

continue_play = True
while continue_play and player.get_money() > 0:
    dealer.reset()
    player.reset()
    player_bet = 0
    while player_bet <= 0 or player_bet > player.get_money():
        player_bet = int(input("How much do you want to bet? "))
        if player_bet <= 0:
            print("Bet must be greater than 0.")
        elif player_bet > player.get_money():
            print("Bet must be less than your current balance: ", player.get_money())
    player.bet(player_bet)
    player.receive_card(dealer.deal())
    player.receive_card(dealer.deal())
    dealer.receive_card(dealer.deal())
    dealer.receive_card(dealer.deal())
    continue_hit = True
    if player.get_score() == 21:
        if dealer.get_score() == 21:
            player.draw()
            print("It's a draw.")
        else:
            player.win()
            print("You win.")
        print("Your hand: ", player.get_cards())
        print("Dealer's hand: ", dealer.get_dealer_card())
        print("Your current balance: ", player.get_money())
        continue_play = input("Type 'y' to play again, type any key exit the game: ").lower() == 'y'
        continue

    print(f"Dealer's first card: {dealer.get_dealer_card()[0]}")
    while continue_hit:
        print(f"Your cards: {player.get_cards()}")
        if player.get_score() > 21:
            print("You went over. You lose.")
            continue_hit = False
        else:
            choice = input("Type 'y' to get another card, 's' to surrender, 'd' to double, or any key to stop: ").lower()
            if choice == 'y':
                player.receive_card(dealer.deal())
            elif choice == 's':
                player.surrender()
                continue_hit = False
                continue_play = input("Type 'y' to play again, type any key to exit the game: ").lower() == 'y'
                continue
            elif choice == 'd':
                if player.get_money() < player.get_bet_amount():
                    print("You don't have enough money to double.")
                    continue
                player.bet(player.get_bet_amount())
                player.receive_card(dealer.deal())
                continue_hit = False
            else:
                continue_hit = False
    while dealer.get_score() < 17:
        dealer.receive_card(dealer.deal())
    print('-' * 20)
    print(f"Your final hand: {player.get_cards()}")
    print(f"Dealer's final hand: {dealer.get_dealer_card()}")
    print('-' * 20)
    print(player.get_score())
    print(dealer.get_score())
    if player.get_score() > 21:
        print("You went over. You lose.")
        player.lose()
    elif dealer.get_score() > 21:
        print("Dealer went over. You win.")
        player.win()
    elif player.get_score() > dealer.get_score():
        print("You win.")
        if player.get_score() == 21:
            player.blackjack()
        else:
            player.win()
    elif player.get_score() == dealer.get_score():
        print("It's a draw.")
        player.draw()
    else:
        print("You lose.")
    print('-' * 20)
    print("Your current balance: ", player.get_money())
    if player.get_money() == 0:
        print("You broke. Game over.")
        break
    continue_play = input("Type 'y' to play again, type any key exit the game: ").lower() == 'y'
print('-' * 20)
print("Summarizing your game:")
print(f"Your final balance: {player.get_money()}")
print("Goodbye!")
