# Exercício Sistema de Pagamaento:

class Usuario:
    def __init__(self, nome, email, senha, saldo=0.0):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.saldo = saldo

class Pagamento:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = float(valor)
        self.status = 'pendente'
    def processar(self):
        if self.valor <= 0:
           self.status = 'falha'
           print(f'Pagamento falhou: valor inválido({self.valor}).')
        return True 
        
usuario = Usuario('Felipe', 'felipe@gmail.com', 1234, saldo=10.0)
pag = Pagamento(usuario, 40.0)
pag.processar()

pag2 = Pagamento(usuario, -5)
pag2.processar()
print('\n -- Resultado final do usuário --')
print(f'{usuario.nome} - Saldo: {usuario.saldo} - Último pagamento status: {pag2.status}')
