from src.NumberAscOrder import *
import pytest
import random

def test_6posicoescom6numSorteados():
    
    cut = NumberAscOrder(6)

    numerosSorteados = [10,30,50,60,5,2]


    for numero in numerosSorteados:
        cut.sortearNUmero(numero)

    numerosOrdenados = cut.sort()

    assert numerosOrdenados == sorted(numerosSorteados)

def test_6posicoescom6numsorteadosAleatorios():

    cut = NumberAscOrder(6)


    numerosSorteio = [random.randint(0,100) for x in range(6)]

    for numero in numerosSorteio:
        cut.sortearNUmero(numero)
    
    numerosOrdenados = cut.sort()

    assert numerosOrdenados == sorted(numerosSorteio)



def test_pilhavazia():
    cut = NumberAscOrder(6)

    with pytest.raises(ValueError, match="erro, pilha vazia"):
        cut.sort()