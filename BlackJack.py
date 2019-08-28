#############################################
#INTERACTIVE BLACKJACK GAME MADE WITH 
#JETBRAINS' PYCHARM IN PYTHON 3 
#THE GAME REPRESENTS A CASINO BLACKJACK
#GAME WITH THE PLAYER AGAINST THE DEALER
#############################################



import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing= True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit

        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


# MAKING THE DECK FOR EACH GAME

class Deck():

    def __init__(self):

        # START WITH AN EMPTY LIST

        self.deck = []

        # ADD EACH CARD INTO THE DECK

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):

        # STRING REPRESENTATION OF DECK

        deck_as_str = ''
        for card in self.deck:
            deck_as_str += '\n' + card.__str__()

        return 'the deck has: ' + deck_as_str

    def shuffle(self):

        # SHUFFLE DECK

        random.shuffle(self.deck)

    def deal(self):

        single_card = self.deck.pop()
        return single_card


class Hand():

    def __init__(self):

        self.cards = []  # START WITH NOTHING
        self.value = 0  # SUM OF CARDS AT START IS 0
        self.aces = 0  # SPECIAL RULE FOR ACES

    def add_card(self, card):

        # CARD PASSED IN IS FROM DECK.DEAL()

        self.cards.append(card)

        # ADD TO VALUE OF HAND

        self.value += values[card.rank]

        # TRACK ACES

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        # IF TOTAL VALUE IS MORE THAN 21 AND THERE IS AN ACE, CHANGE VALUE OF ACE TO 1

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input('How many chips do you want to bet? '))

        except:
            print('Sorry please enter a number')

        else:
            if chips.bet > chips.total:
                print('You do not have enough chips for this bet! You have {}'.format(chips.total))
            else:
                break

def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Do you want to hit or stand? ')
        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("The player stands. Dealer's turn")
            playing = False


        else:
            print('Try again!')
            continue

        break


def player_busts(player, dealer, chips):
    print('Player bust! Dealer wins')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Player wins! Dealer busts')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer wins!')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and player tie! PUSH')


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep = '\n')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep = '\n')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep = '\n')
    print("Player's Hand =", player.value)


# PLAYER'S CHIPS
player_chips = Chips()

while True:
    print('Welcome to BlackJack')

    # CREATE AND SHUFFLE THE DECK. THEN DEAL TWO CARDS TO EACH PLAYER

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # PROMPT BET
    take_bet(player_chips)

    # SHOW CARDS

    show_some(player_hand, dealer_hand)

    while playing:
        # PROMPT HIT OR STAND
        hit_or_stand(deck, player_hand)

        # SHOW CARDS, BUT KEEP ONE OF DEALERS HAND HIDDEN

        show_some(player_hand, dealer_hand)

        # HAS PLAYER BUSTED

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:  # SOFT 17 CASINO RULE
            hit(deck, dealer_hand)

        # SHOW ALL CARDS

        show_all(player_hand, dealer_hand)

        # CHECK SCENARIOS
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # PLAYER'S CHIPS
    print("\n Player's total chips are {}".format(player_chips.total))

    # NEW GAME?

    new_game = input('would you like to play again? y/n: ')

    if new_game[0].lower() == 'y':
        playing = True

    else:
        print('Thank you for playing!')
        break

