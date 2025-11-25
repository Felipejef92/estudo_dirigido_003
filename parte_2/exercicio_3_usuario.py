# Sistema de usuários com POO

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def autenticar(self, email, senha):
        if self.email == email and self.senha == senha:
            return True
        return False
    
usuario1 = Usuario('Felipe', 'felipe@gmail.com', '1234')
usuario2 = Usuario('Juliana', 'juliana@gmail.com', 'abcd')

print('Teste 1 (corrreto):', usuario1.autenticar('felipe@gmail.com', '1234'))
print('Teste 2 (email errado):', usuario1.autenticar('x@gmail.com', '1234'))
print('Teste 3 (senha errada):', usuario1.autenticar('felipe@gmail.com', '9999'))
print('Teste 4 (outro usuário):', usuario2.autenticar('juliana@gmail.com', 'abcd'))
    