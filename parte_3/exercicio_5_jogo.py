# Exercicio jogo:
class jogador:
    def __init__(self,nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.itens = []

    def adicionar_saldo(self, valor):
        self.saldo += valor

    def comprar_item(self, item, preco):
        if self.saldo >= preco:
            self.saldo -= preco
            self.itens.append(item)
            print(f'{self.nome} comprou {item} por R$ {preco}.')
        else:
            print('Saldo insutficiente para comprar esse item.')

jogador1 = jogador('Felipe', 100)
jogador2 = jogador('Juliana', 50)

jogador1.comprar_item('Espada', 60)
jogador1.comprar_item('Escudo', 30)

jogador2.adicionar_saldo(30)
jogador2.comprar_item('Poção de Vida', 40)

print('\n--- Resultado Final ---')
print(f'{jogador1.nome} - Saldo: {jogador1.saldo} - Itens: {jogador1.itens}')
print(f'{jogador2.nome} - Saldo: {jogador2.saldo} - Itens: {jogador2.itens}')


