# Sistema de pedidos 
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(f'- {p.nome} (R$ {p.preco})')

    def calcular_total(self):
        total = 0
        for p in self.produtos:
            total += p.preco
        return total
        
p1 = Produto('Café', 8.5)
p2 = Produto('Bolo', 12.0)
p3 = Produto('Suco', 7.0)

pedido = Pedido()

pedido.adicionar_produto(p1)
pedido.adicionar_produto(p2)
pedido.adicionar_produto(p3)
print('Produtos do pedido:')
pedido.listar_produtos()
print('\nValor total do pedido:', pedido.calcular_total())