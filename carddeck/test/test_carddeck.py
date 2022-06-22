import pytest
from ..carddeck import FrenchDeck

"""
Livro: Python Testing with pytest: Simple, Rapid, Effective, and Scalable
Brian Okken

Anatomia do teste. O teste é formado por 3 etapas (metodologia GWT ou AAA) :

GWT ----------------
- Given - Dado
- When  - Quando
- Then  - Então

AAA ----------------
- Arrange - Arrume, Coloque os dados
- Act - Acione o teste
- Assert - Realize o a verificação do teste

+================
| Principais parâmetros do pytest na linha de comando
+================
--pdb:
    ll - lista o código fonte que está sob o debug
    q - sai do modo debug
    nome_de_variável ou função - exibe o valor
    h - exibe help do debug
-v: exibe modo verboso com nome dos teste
-s: mostra as saídas no console, ex. um print() chamado dentro de um teste
-k "parte_do_nome_de_um_teste": filtra os teste que serão executados
-x: saída rápida, ou seja encerra a execução dos testes ao encontra a primeira 
falha
-rs: exibe o teste e se tiver a razão pelo qual o teste foi pulado
--junitxml path_e_nome_arquivo.xml: cria um relatório dos testes em xml no 
formato Junit, padrão dos frameworks de testes

+================
| Resumo dos principais resultado sobre os testes:
+================
. - passou
F - falhou
x - falha esperada
X - falha esperada, mas não falhou
s - pulou teste
+================
| Mark: cria tags, marcações para testes que podem ser executados apenas eles.
| Vai selecionar o teste pelo nome atribuído a tag e coloca ele em um grupo
| podem ser executados juntos, sinalizar para não serem executados
+================
Ex.
from pytest import mark
@mark.tag
def test_meu_teste_marcado():
    assert True

# executa todos os testes com a tag tag
pytest -m tag

# não executa todos os testes com a tag tag
pytest -m "not tag"

+----------------
| Marcadores embutidos (built-in)
+----------------
@mark.skip : Utilizada para pular um determinado teste
@mark.skipif : Utilizada para pular um teste em determinado contexto
@mark.xfail : Esperado que o teste falhe em algum contexto
@mark.userfixture : ... 
@mark.parametrize : parametriza testes, realizando vários teste semelhante a 
subtests.
Ex.
# função
def soma_mais_2(num):
    return num + 2
# teste da função parametrizado com uma string contendo os nomes dos parâmetros 
# separados por virgula e uma lista de tuplas com valores dos parâmetros: 
# (entrada, valor esperado)
@mark.parametrize(
    'entrada,esperado',
    [(1, 3), (3, 5), (5, 7)]
)
def test_soma_mais_2(estrada, esperado):
    assert soma_mais_2(entrada) == esperado
# serão executados três testes distintos

+----------------
| xfail e skipif 1h23mim
+----------------

"""


@pytest.fixture
def card_deck():
    return FrenchDeck()


def test_amount_cards_in_deck(card_deck):
    """ card_deck - SUT System Under Test """
    entrada = card_deck  # dado
    esperado = 52  # dado

    resultado = len(entrada)  # quando

    assert resultado == esperado  # então

    # TDD - Kent Beck - One-step Test (versão resumida da anatomia do teste)
    assert len(card_deck) == 52


@pytest.mark.parametrize(
    'card,order',
    [
        (26, 0),
        (13, 1),
        (39, 2),
        (0,  3),
    ]
)
def test_order_of_cards_in_deck(card_deck, card, order):
    assert FrenchDeck.order_of_card(card_deck[card]) == order
