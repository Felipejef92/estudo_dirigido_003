 # Exercício Gestão de fncionários

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome 
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f'{self.nome} recebeu um aumento de {percentual}% (+R$ {aumento:.2f}).')

f1 = Funcionario('Felipe', 'Desenvolverdor senior', 8000)
f2 = Funcionario('Juliana', 'Analista de dados', 6000)

f1.aumentar_salario(10)
f2.aumentar_salario(5)

print('\n--- Resultado Final ---')
print(f'{f1.nome} - Cargo: {f1.cargo} - Salário: R$ {f1.salario:.2f}')
print(f'{f2.nome} - Cargo: {f2.cargo} - Salário: R$ {f2.salario:.2f}')
