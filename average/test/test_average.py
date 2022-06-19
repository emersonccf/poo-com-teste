import pytest
from ..average import Average


@pytest.fixture
def avg_template():
    avg = Average()
    avg(10)
    avg(5)
    avg(9)
    return avg


def test_average(avg_template):
    assert avg_template.avg == 8


# @pytest.mark.skip
def test_soma_serie_value(avg_template):
    assert avg_template.sum_serie == 24


def test_length_serie(avg_template):
    assert len(avg_template) == 3
