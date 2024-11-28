from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = round(preco, 2)
        
    @abstractmethod
    def aplicar_desconto(self):
        pass