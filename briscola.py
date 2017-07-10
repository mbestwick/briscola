""" A game of briscola. """

from deck import ShuffledDeck


class Player(object):
    """ A player of briscola. """

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0

    def __repr__(self):
        return "<Player: %s, points: %s, hand: %s>" % (self.name,
                                                       self.points,
                                                       self.hand)


class Game(object):
    """ A game of briscola. """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.playing_deck = ShuffledDeck()
        self.briscola = self.playing_deck.tail

        for i in range(3):
            self.player2.hand.append(self.playing_deck.pick_card())
            self.player1.hand.append(self.playing_deck.pick_card())

    def play_hand(self, lead, follow):
        """ One hand of the game. """

        print "Lead:", lead.name, lead.hand
        discard1 = int(raw_input("Which card would you like to play?\n> "))
        card1 = lead.hand.pop(discard1)
        print "Follow:", follow.name, follow.hand
        discard2 = int(raw_input("Which card would you like to play?\n> "))
        card2 = follow.hand.pop(discard2)

        if card1.suit == card2.suit == self.briscola.suit:
            if card1.rank > card2.rank:
                winner, loser = lead, follow
            else:
                winner, loser = follow, lead
        elif card1.suit == self.briscola.suit:
            winner, loser = lead, follow
        elif card2.suit == self.briscola.suit:
            winner, loser = follow, lead
        elif card1.suit == card2.suit:
            if card1.rank > card2.rank:
                winner, loser = lead, follow
            else:
                winner, loser = follow, lead
        else:
            winner, loser = lead, follow

        print "%s wins the hand!" % winner.name
        winner.points += card1.points + card2.points

        if self.playing_deck.count > 0:
            winner.hand.append(self.playing_deck.pick_card())
            loser.hand.append(self.playing_deck.pick_card())

        if winner.hand:
            self.play_hand(winner, loser)
        else:
            print "%s: %s points" % (self.player1.name, self.player1.points)
            print "%s: %s points" % (self.player2.name, self.player2.points)
            if self.player1.points > 60:
                print "%s wins!!!" % self.player1.name
            else:
                print "%s wins!!!" % self.player2.name


lorenzo = Player('Lorenzo')
luca = Player('Luca')
game = Game(lorenzo, luca)
print game.briscola
game.play_hand(lorenzo, luca)
