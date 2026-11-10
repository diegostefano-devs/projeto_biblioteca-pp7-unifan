from mysql.connector import Error, IntegrityError
import livros

def ler_inteiro(mensagem, obrigatorio=True):
    while True:
        valor = input(mensagem).strip()
        if not valor and not obrigatorio:
            return None
        try:
            return int(valor)
        except ValueError:
            print("Digite um número válido.")

def mostrar(lista):
    if not lista:
        print("Nenhum livro encontrado")
        return
    print(f"\n{'ID':<4} {'Titulo':<35} {'Autor:'<25} {'Ano':>6} Situação")
    print("-" * 85)

    for l in lista:
        situacao = "Disponivel" if l["disponivel"] else "Emprestado"
        ano = l['ano'] or " "
        print(f"{l['id']:<4} {l['titulo'][:34]:<35} {l['autor'][:24]:<25} {ano!s:<6} {situacao}")

def opcao_cadastrar():
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    if not titulo or not autor:
        print("Título e autor são obrigatórios.")
        return
    ano = ler_inteiro("Ano (Enter para pular): ", obrigatorio=False)
    isbn = input("ISBN (Enter para pular): ").strip() or None
    novo_id = livros.cadastrar_livro(titulo, autor, ano, isbn)
    print(f"Livro cadastrado com id {novo_id}.")

def opcao_atualizar():
    livro_id = ler_inteiro("ID do livro: ")
    atual = livros.buscar_por_id(livro_id)
    if not atual:
        print("Livro não encontrado.")
        return
    print("Deixe em branco para manter o valor atual.")
    titulo = input(f"Título [{atual['titulo']}]: ").strip() or atual["titulo"]
    autor = input(f"Autor [{atual['autor']}]: ").strip() or atual["autor"]
    ano = ler_inteiro(f"Ano [{atual['ano']}]: ", obrigatorio=False) or atual["ano"]
    isbn = input(f"ISBN [{atual['isbn']}]: ").strip() or atual["isbn"]
    disp = input("Disponível? (s/n, Enter mantém): ").strip().lower()
    disponivel = atual["disponivel"] if disp == "" else disp == "s"
    livros.atualizar_livro(livro_id, titulo, autor, ano, isbn, disponivel)
    print("Livro atualizado.")

def opcao_excluir():
    livro_id = ler_inteiro("ID do livro: ")
    if input("Tem certeza? (s/n): ").strip().lower() != "s":
        print("Exclusão cancelada.")
        return
    if livros.excluir_livro(livro_id):
        print("Livro excluído.")
    else:
        print("Livro não encontrado.")
def menu():
    while True:
        print("\n===== BIBLIOTECA =====")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Atualizar livro")
        print("5 - Excluir livro")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()
        try:
            if opcao == "1":
                opcao_cadastrar()
            elif opcao == "2":
                mostrar(livros.listar_livros())
            elif opcao == "3":
                mostrar(livros.buscar_livro(input("Título ou autor: ")))
            elif opcao == "4":
                opcao_atualizar()
            elif opcao == "5":
                opcao_excluir()
            elif opcao == "0":
                print("Até logo!")
                break
            else:
                print("Opção inválida.")
        except IntegrityError:
            print("Já existe um livro com esse ISBN.")
        except Error as erro:
            print(f"Erro no banco de dados: {erro}")

if __name__ == "__main__":
    menu()

