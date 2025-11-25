# Sistema de produtos semo POO
def adicionar_estoque(produto, qtd):
    produto['quantidade'] += qtd

def remover_estoque(produto, qtd):
    if qtd > produto['quantidade']:
        print('Erro: quantidade solicitada maior que o estoque disponível. ')
        return 
    produto['quantidade'] -= qtd

def valor_total(produto):
    return produto['quantidade'] * produto['preco']

produto = {'nome': 'Café', 'quantidade': 5, 'preco': 8.50}
adicionar_estoque(produto, 3)
remover_estoque(produto, 2)
total = valor_total(produto)
print(produto)
print('Valor total', total)