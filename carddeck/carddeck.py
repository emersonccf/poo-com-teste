from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def random_card(self):
        return choice(self._cards)


if __name__ == '__main__':
    card_deck = FrenchDeck()
    print('Total de cartas do baralho Francês %d cartas.' % (len(card_deck)))
    print(card_deck[0])
    print(card_deck[13])
    print(card_deck[26])
    # breakpoint() # serve para debugar o código neste ponto via terminal
    # pdb.set_trace() # outra forma de debugar, mais antiga faz a mesma coisa
    print(card_deck[39])
    print(card_deck[-1])
    print(card_deck.random_card())
