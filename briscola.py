""" A game of briscola. """

from deck import ShuffledDeck

rank = ['2', '4', '5', '6', '7', 'Fante', 'Cavallo', 'Re', 'Tre', 'Asso']


class Game(object):
    """ A game of briscola. """

    def __init__(self):
        self.player1 = []
        self.player2 = []
        self.playing_deck = ShuffledDeck()
        self.briscola = self.playing_deck.tail

        for i in range(3):
            self.player2.append(self.playing_deck.pick_card())
            self.player1.append(self.playing_deck.pick_card())

    def play_hand(self, order=1):
        """ One hand of the game. """

        if order == 1:
            lead = {'hand': self.player1, 'name': "Player1"},
            follow = {'hand': self.player2, 'name': "Player2"}
        else:
            lead = {'hand': self.player2, 'name': "Player2"}
            follow = {'hand': self.player1, 'name': "Player1"}

        print "Lead:", lead['name'], lead['hand']
        discard1 = int(raw_input("Which card would you like to play?\n> "))
        card1 = lead['hand'].pop(discard1)
        print "Follow:", follow['name'], follow['hand']
        discard2 = int(raw_input("Which card would you like to play?\n> "))
        card2 = follow['hand'].pop(discard2)

        if card1.suit == card2.suit == self.briscola.suit:
            if rank.index(card1.card) > rank.index(card2.card):
                winner = lead
                print "%s wins the hand." % lead['name']
            else:
                winner = follow
                print "%s wins the hand." % follow['name']
        elif card1.suit == self.briscola.suit:
            winner = lead
            print "%s wins the hand." % lead['name']
        elif card2.suit == self.briscola.suit:
            winner = follow
            print "%s wins the hand." % follow['name']
        else:
            if rank.index(card1.card) > rank.index(card2.card):
                winner = lead
                print "%s wins the hand." % lead['name']
            else:
                winner = follow
                print "%s wins the hand." % follow['name']

        if winner['name'] == "Player1":
            if self.playing_deck.count > 6:
                self.player1.append(self.playing_deck.pick_card())
                self.player2.append(self.playing_deck.pick_card())
            if self.playing_deck.count == 0:

        else:
            self.player2.append(self.playing_deck.pick_card())
            self.player1.append(self.playing_deck.pick_card())



