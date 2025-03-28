# pylint: disable=C0114, C0301
import random
class BlackJackDealer:
    """The dealer class for the blackjack game"""
    def __init__(self, deck = 1):
        self.deck = deck
        self.score = 0
        self.cards = [ 4 * deck for x in range(0, 13)]
        self.points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.dealer_card = []

    def deal(self):
        """Deal a card to the player

        Returns:
            int: The card dealt to the player
        """
        card = random.randint(0, 12)
        while self.cards[card] == 0:
            card = random.randint(0, 12)
        self.cards[card] -= 1
        return card

    def get_score(self):
        """Get the current score of the dealer
        
        Returns:
            int: The current score of the dealer
        """
        return self.score

    def reset(self):
        """Reset the dealer's score to 0 and the cards to the original state
        """
        self.score = 0
        self.cards = [ 4 * self.deck for x in range(0, 13)]
        self.dealer_card = []

    def get_dealer_card(self):
        """Get the dealer's card
        
        Returns:
            int: The dealer's card
        """
        return self.dealer_card

    def receive_card(self, card):
        """Get the cards for the dealer
        
        Args:
            int: The card dealt to the dealer
        """
        if(card == 0 and self.score + 11 <= 21):
            self.score += 11
        else:
            self.score += self.points[card]

        if card == 0:
            card = 'A'
        elif card == 10:
            card = 'J'
        elif card == 11:
            card = 'Q'
        elif card == 12:
            card = 'K'
        else:
            card += 1

        self.dealer_card.append(card)

class BlackJackPlayer:
    """The player class for the blackjack"""
    def __init__(self, money = 100):
        self.score = 0
        self.cards = []
        self.points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.money = money
        self.bet_amount = 0

    def receive_card(self, card):
        """Get the cards for the player
        
        Args:
            int: The card dealt to the player
        """
        if(card == 0 and self.score + 11 <= 21):
            self.score += 11
        else:
            self.score += self.points[card]

        if card == 0:
            card = 'A'
        elif card == 10:
            card = 'J'
        elif card == 11:
            card = 'Q'
        elif card == 12:
            card = 'K'
        else:
            card += 1

        self.cards.append(card)

    def get_score(self):
        """Get the current score of the player
        
        Returns:
            int: The current score of the player
        """
        return self.score

    def reset(self):
        """Reset the player's score to 0 and the cards to an empty list"""
        self.score = 0
        self.cards = []
        self.bet_amount = 0

    def get_cards(self):
        """Get the player's cards
        
        Returns:
            list: The player's cards
        """
        return self.cards

    def get_money(self):
        """Get the player's money
        
        Returns:
            int: The player's money
        """
        return self.money

    def bet(self, amount):
        """Place a bet for the player
        
        Args:
            int: The amount of the bet
        """
        assert amount <= self.money, ("You don't have enough money to place that bet. Your current balance is ", self.money)
        self.money -= amount
        self.bet_amount += amount

    def get_bet_amount(self):
        """Get the bet amount
        
        Returns:
            int: The amount of the bet
        """
        return self.bet_amount

    def win(self):
        """The player wins the game"""
        self.money += 2 * self.bet_amount
        self.bet_amount = 0

    def lose(self):
        """The player loses the game"""
        self.bet_amount = 0

    def draw(self):
        """The player draws the game"""
        self.money += self.bet_amount
        self.bet_amount = 0

    def surrender(self):
        """The player surrenders the game"""
        self.money += self.bet_amount / 2
        self.bet_amount = 0

    def blackjack(self):
        """The player gets a blackjack"""
        self.money += 2.5 * self.bet_amount
        self.bet_amount = 0
