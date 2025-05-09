from src.custom_stack_class import *

class NumberAscOrder:
    def __init__(self, plimt):
        self.pilha = CustomStack(plimt)

    def sortearNUmero(self, valor):
        self.pilha.push(valor)

    def sort(customStack):

        if customStack.pilha.is_empty():
            raise ValueError("erro, pilha vazia")

        numeroOrdenados = list(customStack.pilha.elements)
        return sorted(numeroOrdenados)
