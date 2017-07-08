""" A shuffled deck for the game (using linked list). """

from cards import Deck
from random import randint

deck = Deck()


class ShuffledDeck(object):
    """ Shuffled Deck using Linked List with head and tail. """

    def __init__(self):
        self.head = deck.cards.pop(randint(0, len(deck.cards) - 1))
        self.tail = None
        self.count = 40

        curr = self.head
        while len(deck.cards) > 1:
            curr.next = deck.cards.pop(randint(0, len(deck.cards) - 1))
            curr = curr.next

        curr.next = deck.cards.pop()
        self.tail = curr.next

    def pick_card(self):
        """ Picks top card in the shuffled deck. """

        picked_card = self.head
        self.head = self.head.next
        self.count -= 1

        return picked_card

    def __repr__(self):
        return "<Shuffled Deck, tail: %s, count: %s>" % (self.tail, self.count)
