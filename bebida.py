from item_cardapio import ItemCardapio

class Bebida(ItemCardapio): 
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self.preco = round(self.preco*0.92, 2)  
        