""" The cards for the game. """


points = {'Asso': 11, 'Tre': 10, 'Re': 4, 'Cavallo': 3, 'Fante': 2}
rank = ['2', '4', '5', '6', '7', 'Fante', 'Cavallo', 'Re', 'Tre', 'Asso']


class Card(object):
    """ A card for the game. """

    def __init__(self, suit, card):
        self.suit = suit
        self.card = card
        self.points = points.get(card, 0)
        self.rank = rank.index(card)
        self.next = None

    def __repr__(self):
        return "<%s di %s: %s pts>" % (self.card, self.suit, self.points)


class Deck(object):
    """ A deck of complete cards. """

    def __init__(self):
        self.cards = [Card('Dinari', 'Asso'),
                      Card('Dinari', 'Tre'),
                      Card('Dinari', 'Re'),
                      Card('Dinari', 'Cavallo'),
                      Card('Dinari', 'Fante'),
                      Card('Dinari', '7'),
                      Card('Dinari', '6'),
                      Card('Dinari', '5'),
                      Card('Dinari', '4'),
                      Card('Dinari', '2'),
                      # Coppe
                      Card('Coppe', 'Asso'),
                      Card('Coppe', 'Tre'),
                      Card('Coppe', 'Re'),
                      Card('Coppe', 'Cavallo'),
                      Card('Coppe', 'Fante'),
                      Card('Coppe', '7'),
                      Card('Coppe', '6'),
                      Card('Coppe', '5'),
                      Card('Coppe', '4'),
                      Card('Coppe', '2'),
                      # Spade
                      Card('Spade', 'Asso'),
                      Card('Spade', 'Tre'),
                      Card('Spade', 'Re'),
                      Card('Spade', 'Cavallo'),
                      Card('Spade', 'Fante'),
                      Card('Spade', '7'),
                      Card('Spade', '6'),
                      Card('Spade', '5'),
                      Card('Spade', '4'),
                      Card('Spade', '2'),
                      # Bastoni
                      Card('Bastoni', 'Asso'),
                      Card('Bastoni', 'Tre'),
                      Card('Bastoni', 'Re'),
                      Card('Bastoni', 'Cavallo'),
                      Card('Bastoni', 'Fante'),
                      Card('Bastoni', '7'),
                      Card('Bastoni', '6'),
                      Card('Bastoni', '5'),
                      Card('Bastoni', '4'),
                      Card('Bastoni', '2')]

    def __repr__(self):
        return "<Deck>"
