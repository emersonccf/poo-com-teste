import pytest
from ..carddeck import FrenchDeck


@pytest.fixture
def card_deck():
    return FrenchDeck()


def test_qtd_card_deck(card_deck):
    assert len(card_deck) == 52
