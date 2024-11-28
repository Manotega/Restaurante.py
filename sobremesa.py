from item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.descricao = descricao
    
    def __str__(self):
        return self.nome
    
    def aplicar_desconto(self):
        self.preco = round(self.preco*0.85)
        