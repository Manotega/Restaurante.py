from classe_restaurante import Restaurante 
from prato import Prato
from bebida import Bebida    


lucas_pizza = Restaurante('pizzaria Lucas', 'Pizzaria')
lucas_pizza.receber_avaliacao('cleber', 5)
lucas_pizza.receber_avaliacao('coiso', 5)
lucas_pizza.receber_avaliacao('rique', 4)

mexicano = Restaurante('Taco Bell', 'Mexicano')
mexicano.receber_avaliacao('rique', 4)
mexicano.receber_avaliacao('rique', 4)
mexicano.receber_avaliacao('rique', 3)

prato1 = Prato('linguica', 10.00, 'Calma calabreso')
prato2 = Prato('Jordan', 10.00, 'receba')
bebida1 = Bebida('suco de ', 8.95, 'G')
bebida2 = Bebida('Coca', 8.95, 'M')
prato1.aplicar_desconto()
bebida1.aplicar_desconto()

lucas_pizza.adicionar_no_cardapio(prato1)
lucas_pizza.adicionar_no_cardapio(prato2)
lucas_pizza.adicionar_no_cardapio(bebida1)
lucas_pizza.adicionar_no_cardapio(bebida2)
    
lucas_pizza.exibir_cardapio



def main():
    pass
    
if __name__ == '__main__':
    main()
