import pytest
from ..carddeck import FrenchDeck

"""
+================
| Pytest: Uma introdução - Live de Python #167 Eduardo Mendes (YouTube)
+================
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

xUnit Patterns - Gerard Mezaros : um teste não é composto apenas de 3 etapas e
sim de 4 passos (four steps pass)

- Setup     - Dado
- Exercise  - Quando
- Verify    - Então
- TearDown  - "Desmonta tudo antes que seja tarde"

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
| xfail e skipif 
+----------------
Dizem quando:
1- xfail: um teste deve falhar, pois é esperado que ele falhe;
2- skipif: e quando um teste não deve ser executado;

Ex. 2
import sys

@mark.skipif(
    sys.platform == "win32",
    reason="Não funciona no windows"
)
def test_soma_mais_2():
    numero_do_pinguim = 42
    assert soma_mais_2(numero_do_pinguim) == 42

Ex. 1
@mark.xfail() ou @mark.xfail(sys.platform == "win32")
def test_fun():
    pass

+================
| Fixtures : uma introdução muito sutil sobre este assunto ... 1h40
+================
Maneira de "entrar" em um contexto ou prover ferramenta ou algo que precisa ser
executado antes e depois dos testes.

Casos de uso:
1- Espionar a saída padrão do sistema (sys.stdout), para saber se determinada 
saída foi enviada / exibida;
    tipos: 
        - capsys - monitora o stdout;
        - tempdir - cria um diretório temporário;
        - caplog - espiona log's;
        - mokeypach - adiciona atributos e métodos a objetos em runtime;  
        - etc. ...
Ex.
def greeting(greet):
    print(greet)

def teste_greeting_output(capsys):
    greeting('Como vai!')
    captured = capsys.redouterr()
    assert captured.out == 'Como vai!\n'

O grande poder do pytest está em criar nossas próprias fixtures!

Moke: Dublês de teste live  Eduardo Mendes#76 - assistir depois

+================
| Pytest Fixtures - Live de Python #168 Eduardo Mendes (YouTube)
+================
Livros recomendados:
    * Teoria geral dos teste:
        x- Test-Driven development by Example
        - Growing Object-Oriented Software Guided by Tests
        - xUnit Test Pattens: Refectory Test Code
    * sobre o Pytest:
        - Unit Testing: Principles, Practices and Pattens 
        x- Python Test with Pytest: Simple, Rapid, Efficient and Scalable 
        x- Pytest Quick Start Guide, em PDF disponível na internet do brasileiro
        que contribui com o projeto do pytest (Bruno Oliveira) - 
        Repositório: https://github.com/PacktPublishing/pytest-Quick-Start-Guide


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
        (0,  0),
        (13, 1),
        (26, 2),
        (39, 3),
    ]
)
def test_order_of_cards_in_deck(card_deck, card, order):
    assert FrenchDeck.order_of_card(card_deck[card]) == order


def test_name_deck_card(capsys, card_deck):
    # exemplo de fixture: capsys (monitora a saída sys.stdout)
    card_deck.print_name_class_card_deck()
    captured = capsys.readouterr()
    assert captured.out == 'FrenchDeck\n'
