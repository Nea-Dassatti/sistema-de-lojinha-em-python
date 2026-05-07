# Programa de gerenciamento de livros
# Autor: [Cleidinea Dassatti]

# Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Gerenciamento de Livros! Desenvolvido por [Cleidinea dassatti]")

# Inicialização da lista de livros e variável id_global
lista_livro = []
id_global = 0

# Função para cadastrar um novo livro
def cadastrar_livro(id):
    print("\n=== Cadastrar Livro ===")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    
    # Criando dicionário com os dados do livro
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    
    # Adicionando o livro à lista
    lista_livro.append(livro)
    print(f"Livro '{nome}' cadastrado com sucesso!")

# Função para consultar livros
def consultar_livro():
    while True:
        print("\n=== Consultar Livro ===")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            # Consultar todos os livros
            if not lista_livro:
                print("Nenhum livro cadastrado.")
            else:
                print("\nLista de todos os livros:")
                for livro in lista_livro:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
        
        elif opcao == "2":
            # Consultar por ID
            try:
                id_busca = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_busca:
                        print(f"\nLivro encontrado:")
                        print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Id inválido")
            except ValueError:
                print("Id inválido")
        
        elif opcao == "3":
            # Consultar por autor
            autor_busca = input("Digite o nome do autor: ")
            encontrados = False
            print(f"\nLivros do autor {autor_busca}:")
            for livro in lista_livro:
                if livro['autor'].lower() == autor_busca.lower():
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    encontrados = True
            if not encontrados:
                print("Nenhum livro encontrado para este autor.")
        
        elif opcao == "4":
            # Retornar ao menu principal
            break
        
        else:
            print("Opção inválida")

# Função para remover livro
def remover_livro():
    while True:
        try:
            id_remover = int(input("\nDigite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro['id'] == id_remover:
                    lista_livro.remove(livro)
                    print(f"Livro com ID {id_remover} removido com sucesso!")
                    return
            print("Id inválido")
        except ValueError:
            print("Id inválido")

# Menu principal
def main():
    global id_global
    while True:
        print("\n=== Sistema de Gerenciamento de Livros ===")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            # Cadastrar novo livro
            id_global += 1
            cadastrar_livro(id_global)
        
        elif opcao == "2":
            # Consultar livros
            consultar_livro()
        
        elif opcao == "3":
            # Remover livro
            remover_livro()
        
        elif opcao == "4":
            # Encerrar programa
            print("Programa encerrado. Até logo!")
            break
        
        else:
            print("Opção inválida")

# Executar o programa
if __name__ == "__main__":
    main()