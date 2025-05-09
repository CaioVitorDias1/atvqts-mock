from src.custom_stack_class import *
import pytest

def test_push_one_elementinstack():
    element_value = 5.0
    value = 0.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()

def test_sePilhalotada():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2.0)
    cut.push(3)

    with pytest.raises(StackFullException):
        cut.push(5)


def test_pilhavazia():
    cut = CustomStack(5)

    with pytest.raises(StackEmptyException):
        cut.top()

def test_pilhavaziaPop():
    cut = CustomStack(5)

    with pytest.raises(StackEmptyException):
        cut.pop()

def test_elemetnp():
    cut = CustomStack(5)

    cut.push(5)

    elemento = cut.pop()

    assert elemento == 5
    assert cut.is_empty()