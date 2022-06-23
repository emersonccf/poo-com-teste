import pytest
from ..vector import MultiplyTypeDifferentError, Vector, AddTypeDifferentError


@pytest.fixture
def v1():
    return Vector(2, 4)


@pytest.fixture
def v2():
    return Vector(2, 1)


def test_representation_vector(v1, v2):
    assert repr(v1) == 'Vector(2, 4)'
    assert repr(v2) == 'Vector(2, 1)'


def test_equal_between_vectores():
    assert Vector() == Vector()


def test_different_between_vectores(v1, v2):
    assert v1 != v2


def test_add_vectores(v1, v2):
    v = v1 + v2
    assert v == Vector(4, 5)


def test_add_types_different(v1):
    try:
        v1 + 4
    except AddTypeDifferentError as error:
        assert type(error) is AddTypeDifferentError


def test_value_absolute_vector(v1, v2):
    assert abs(v1) == 4.47213595499958
    assert abs(v2) == 2.23606797749979


def test_multiply_vector_for_integer(v1, v2):
    vi = v1 * 3
    vii = v2 * 3
    assert vi == Vector(6, 12)
    assert vii == Vector(6, 3)


def test_multiply_types_different(v1, v2):
    try:
        v1 * v2
    except MultiplyTypeDifferentError as error:
        assert type(error) is MultiplyTypeDifferentError


def test_boolean_vector(v1, v2):
    assert bool(v1) is True
    assert bool(v2) is True
    assert bool(Vector()) is False
