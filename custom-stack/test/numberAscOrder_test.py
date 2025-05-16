from src.NumberAscOrder import *
import pytest
from unittest.mock import MagicMock, call, patch
import random

def test_6posicoescom6numSorteados():
    
    #Gerando mockk
    mock_stack = MagicMock()
    
    
    mock_stack.is_empty.return_value = False
    # valores estaticos na listaa
    
    mock_stack.elements = [10, 30, 50, 60, 5, 2]

    # Cria a instância de NumberAscOrder e injeta o mock
    cut = NumberAscOrder(6)
    cut.pilha = mock_stack  # substitui a pilha real pelo mock

    #metodo de ordenação
    resultado = cut.sort()

    # Valida se o resultado está ordenado corretamente
    assert resultado == sorted(mock_stack.elements)
    mock_stack.is_empty.assert_called_once()

# def test_6posicoescom6numsorteadosAleatorios():

#     cut = NumberAscOrder(6)


#     numerosSorteio = [random.randint(0,100) for x in range(6)]

#     for numero in numerosSorteio:
#         cut.sortearNUmero(numero)
    
#     numerosOrdenados = cut.sort()

#     assert numerosOrdenados == sorted(numerosSorteio)



def test_pilhavazia():

    mock_stack = MagicMock()
    mock_stack.is_empty.return_value = True  # forçar pilha vazia
    mock_stack.elements = []

    cut = NumberAscOrder(6)
    cut.pilha = mock_stack

    with pytest.raises(ValueError, match="erro, pilha vazia"):
        cut.sort()

    mock_stack.is_empty.assert_called_once()