# Sistema de produtos com POO
class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def adicionar(self, qtd):
        self.quantidade += qtd

    def remover(self, qtd):
        if qtd > self.quantidade:
            print('Erro: quantidade excede o estoque.' )
            return
        self.quantidade -= qtd

    def valor_total(self):
        return self.quantidade * self.preco
    
produto = Produto('café', 5, 8.5)
produto.adicionar(3)
produto.remover(2)
total = produto.valor_total()
print(vars(produto))
print('Valor total:', total)