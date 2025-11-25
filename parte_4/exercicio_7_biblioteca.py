# Exercício Sistema de biblioteca
class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

class Biblioteca:
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f' Livro "{titulo}" emprestado com sucesso. ')
                    return True
                else:
                    print(f' O livro "{titulo}" já está emprestado.')
                    return False
        print(f' O livro "{titulo}" não foi encontrado') 

    def listar_disponiveis(self):
        print('Livros disponíveis: ')
        for livro in self.livros:
            if livro.disponivel:
                print(f' - {livro.titulo} ({livro.autor})')   

 # ---------- TESTES ----------
biblioteca = Biblioteca()

l1 = Livro("Dom Casmurro", "Machado de Assis")
l2 = Livro("O Hobbit", "J.R.R. Tolkien")
l3 = Livro("Clean Code", "Robert Martin")

biblioteca.adicionar_livro(l1)
biblioteca.adicionar_livro(l2)
biblioteca.adicionar_livro(l3)

biblioteca.listar_disponiveis()

print("\n--- Tentando emprestar ---")
biblioteca.emprestar_livro("O Hobbit")

print("\n--- Tentando emprestar de novo ---")
biblioteca.emprestar_livro("O Hobbit")

print("\n--- Disponíveis após emprestar ---")
biblioteca.listar_disponiveis()
    