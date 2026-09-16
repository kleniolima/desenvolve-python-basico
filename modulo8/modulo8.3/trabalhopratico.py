import csv
from collections import namedtuple
from getpass import getpass

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# ==========================================================
# CONFIGURAÇÕES INICIAIS
# ==========================================================

# Arquivo onde ficam salvos os usuários
ARQUIVO_USUARIOS = "usuarios.csv"

# Arquivo onde ficam salvos os produtos
ARQUIVO_PRODUTOS = "produtos.csv"

# Objeto para imprimir mensagens bonitas no terminal
console = Console()

# Estruturas simples para guardar dados
Usuario = namedtuple("Usuario", ["login", "senha", "tipo"])
Produto = namedtuple("Produto", ["id", "nome", "preco", "descricao"])


# ==========================================================
# FUNÇÕES PARA USUÁRIOS
# ==========================================================

def carregar_usuarios(arquivo_csv):
    """
    Lê os usuários do arquivo CSV e devolve um dicionário.

    A chave do dicionário será o login.
    Isso facilita buscar um usuário rapidamente.
    """
    usuarios = {}

    try:
        with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                # Cada linha precisa ter exatamente 3 dados:
                # login, senha e tipo
                if len(linha) != 3:
                    continue

                login, senha, tipo = linha
                usuarios[login] = Usuario(login=login, senha=senha, tipo=tipo)

    except FileNotFoundError:
        # Se o arquivo ainda não existir, começamos com lista vazia
        pass

    return usuarios


def salvar_usuarios(arquivo_csv, usuarios):
    """
    Reescreve o arquivo de usuários inteiro.

    Isso é necessário porque, ao alterar ou excluir,
    precisamos salvar o estado atual completo.
    """
    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        for usuario in usuarios.values():
            escritor.writerow([usuario.login, usuario.senha, usuario.tipo])


def fazer_login(usuarios):
    """
    Solicita login e senha do usuário.
    Se estiver correto, retorna o usuário encontrado.
    Caso contrário, retorna None.
    """
    console.print(Panel("ENTRAR NO SISTEMA", style="cyan"))

    login = Prompt.ask("Login").strip()
    senha = getpass("Senha: ").strip()

    usuario = usuarios.get(login)

    # Verifica se o usuário existe e se a senha confere
    if usuario is not None and usuario.senha == senha:
        console.print("[green]Login realizado com sucesso.[/green]")
        return usuario

    console.print("[red]Login ou senha inválidos.[/red]")
    return None


def cadastrar_usuario(usuarios, usuario_logado):
    """
    Cadastra um novo usuário.

    Regras:
    - Se for admin, pode escolher o tipo do usuário.
    - Se não for admin, o novo usuário será cliente.
    """
    console.print(Panel("CADASTRO DE USUÁRIO", style="green"))

    login = Prompt.ask("Novo login").strip()

    # Evita cadastrar dois usuários com o mesmo login
    if login in usuarios:
        console.print("[red]Este login já existe.[/red]")
        return

    senha = getpass("Nova senha: ").strip()

    # Admin pode escolher o tipo
    if usuario_logado is not None and usuario_logado.tipo == "admin":
        tipo = Prompt.ask("Tipo", choices=["admin", "cliente"], default="cliente")
    else:
        # Usuário comum sempre cria cliente
        tipo = "cliente"

    usuarios[login] = Usuario(login=login, senha=senha, tipo=tipo)
    salvar_usuarios(ARQUIVO_USUARIOS, usuarios)

    console.print("[green]Usuário cadastrado com sucesso.[/green]")


def atualizar_senha(usuarios, usuario_logado):
    """
    Atualiza a senha.

    Regras:
    - Admin pode alterar senha de qualquer usuário.
    - Cliente altera apenas a própria senha.
    """
    console.print(Panel("ATUALIZAR SENHA", style="yellow"))

    # Admin escolhe qual usuário será alterado
    if usuario_logado.tipo == "admin":
        login = Prompt.ask("Login do usuário").strip()

        if login not in usuarios:
            console.print("[red]Usuário não encontrado.[/red]")
            return
    else:
        # Cliente só altera a própria senha
        login = usuario_logado.login

    nova_senha = getpass("Nova senha: ").strip()

    usuario_antigo = usuarios[login]

    # Mantém login e tipo, troca apenas a senha
    usuarios[login] = Usuario(
        login=usuario_antigo.login,
        senha=nova_senha,
        tipo=usuario_antigo.tipo
    )

    salvar_usuarios(ARQUIVO_USUARIOS, usuarios)
    console.print("[green]Senha atualizada com sucesso.[/green]")


def excluir_usuario(usuarios, usuario_logado):
    """
    Exclui um usuário do sistema.

    Regras:
    - Somente admin pode excluir usuários.
    - O admin não pode excluir o próprio login enquanto estiver logado.
    """
    if usuario_logado.tipo != "admin":
        console.print("[red]Apenas admin pode excluir usuários.[/red]")
        return

    console.print(Panel("EXCLUIR USUÁRIO", style="red"))

    login = Prompt.ask("Login do usuário a excluir").strip()

    if login not in usuarios:
        console.print("[red]Usuário não encontrado.[/red]")
        return

    if login == usuario_logado.login:
        console.print("[red]Você não pode excluir o próprio usuário logado.[/red]")
        return

    del usuarios[login]
    salvar_usuarios(ARQUIVO_USUARIOS, usuarios)

    console.print("[green]Usuário excluído com sucesso.[/green]")


# ==========================================================
# FUNÇÕES PARA PRODUTOS
# ==========================================================

def carregar_produtos(arquivo_csv):
    """
    Lê os produtos do arquivo CSV e devolve um dicionário.

    A chave será o ID do produto.
    """
    produtos = {}

    try:
        with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                # Cada linha precisa ter 4 dados:
                # id, nome, preco e descricao
                if len(linha) != 4:
                    continue

                pid, nome, preco, descricao = linha

                # Converte preço para número decimal
                produtos[pid] = Produto(
                    id=pid,
                    nome=nome,
                    preco=float(preco),
                    descricao=descricao
                )

    except FileNotFoundError:
        # Se não existir arquivo, começa sem produtos
        pass

    return produtos


def salvar_produtos(arquivo_csv, produtos):
    """
    Salva todos os produtos novamente no arquivo CSV.
    """
    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        for produto in produtos.values():
            escritor.writerow([
                produto.id,
                produto.nome,
                produto.preco,
                produto.descricao
            ])


def cadastrar_produto(produtos):
    """
    Cadastra um novo produto.
    """
    console.print(Panel("CADASTRO DE PRODUTO", style="green"))

    pid = Prompt.ask("ID do produto").strip()

    if pid in produtos:
        console.print("[red]Este ID já existe.[/red]")
        return

    nome = Prompt.ask("Nome do produto").strip()
    preco_texto = Prompt.ask("Preço").strip()
    descricao = Prompt.ask("Descrição").strip()

    # Converte o preço para float
    try:
        preco = float(preco_texto)
    except ValueError:
        console.print("[red]Preço inválido.[/red]")
        return

    produtos[pid] = Produto(
        id=pid,
        nome=nome,
        preco=preco,
        descricao=descricao
    )

    salvar_produtos(ARQUIVO_PRODUTOS, produtos)
    console.print("[green]Produto cadastrado com sucesso.[/green]")


def atualizar_produto(produtos):
    """
    Atualiza os dados de um produto existente.
    """
    console.print(Panel("ATUALIZAR PRODUTO", style="yellow"))

    pid = Prompt.ask("ID do produto a atualizar").strip()

    if pid not in produtos:
        console.print("[red]Produto não encontrado.[/red]")
        return

    produto_antigo = produtos[pid]

    # Mostra os dados atuais como padrão
    nome = Prompt.ask("Novo nome", default=produto_antigo.nome).strip()
    preco_texto = Prompt.ask("Novo preço", default=str(produto_antigo.preco)).strip()
    descricao = Prompt.ask("Nova descrição", default=produto_antigo.descricao).strip()

    try:
        preco = float(preco_texto)
    except ValueError:
        console.print("[red]Preço inválido.[/red]")
        return

    produtos[pid] = Produto(
        id=pid,
        nome=nome,
        preco=preco,
        descricao=descricao
    )

    salvar_produtos(ARQUIVO_PRODUTOS, produtos)
    console.print("[green]Produto atualizado com sucesso.[/green]")


def excluir_produto(produtos):
    """
    Remove um produto pelo ID.
    """
    console.print(Panel("EXCLUIR PRODUTO", style="red"))

    pid = Prompt.ask("ID do produto a excluir").strip()

    if pid not in produtos:
        console.print("[red]Produto não encontrado.[/red]")
        return

    del produtos[pid]
    salvar_produtos(ARQUIVO_PRODUTOS, produtos)

    console.print("[green]Produto excluído com sucesso.[/green]")


def buscar_produto_por_id(produtos):
    """
    Busca um produto usando o ID.
    """
    console.print(Panel("BUSCAR PRODUTO POR ID", style="cyan"))

    pid = Prompt.ask("Digite o ID").strip()

    produto = produtos.get(pid)

    if produto is None:
        console.print("[red]Produto não encontrado.[/red]")
        return

    console.print(
        Panel(
            f"ID: {produto.id}\n"
            f"Nome: {produto.nome}\n"
            f"Preço: R$ {produto.preco:.2f}\n"
            f"Descrição: {produto.descricao}",
            title="Produto encontrado",
            style="green"
        )
    )


def listar_produtos_ordenados_nome(produtos):
    """
    Exibe os produtos em ordem alfabética pelo nome.
    """
    console.print(Panel("PRODUTOS ORDENADOS POR NOME", style="cyan"))

    lista = sorted(produtos.values(), key=lambda p: p.nome.lower())

    if not lista:
        console.print("[yellow]Nenhum produto cadastrado.[/yellow]")
        return

    for produto in lista:
        console.print(
            f"[bold]{produto.id}[/bold] | {produto.nome} | "
            f"R$ {produto.preco:.2f} | {produto.descricao}"
        )


def listar_produtos_ordenados_preco(produtos):
    """
    Exibe os produtos em ordem crescente de preço.
    """
    console.print(Panel("PRODUTOS ORDENADOS POR PREÇO", style="cyan"))

    lista = sorted(produtos.values(), key=lambda p: p.preco)

    if not lista:
        console.print("[yellow]Nenhum produto cadastrado.[/yellow]")
        return

    for produto in lista:
        console.print(
            f"[bold]{produto.id}[/bold] | {produto.nome} | "
            f"R$ {produto.preco:.2f} | {produto.descricao}"
        )


# ==========================================================
# MENUS
# ==========================================================

def menu_inicial():
    """
    Menu inicial do sistema.
    Aparece antes do login.
    """
    console.print(Panel("SISTEMA DE USUÁRIOS E PRODUTOS", style="blue"))
    print("1 - Login")
    print("2 - Cadastrar usuário")
    print("3 - Sair")

    return Prompt.ask("Escolha uma opção", choices=["1", "2", "3"])


def menu_admin():
    """
    Menu exibido para usuários do tipo admin.
    """
    print("\n1 - Atualizar senha de usuário")
    print("2 - Excluir usuário")
    print("3 - Gerenciar produtos")
    print("0 - Logout")

    return Prompt.ask("Escolha uma opção", choices=["0", "1", "2", "3"])


def menu_cliente():
    """
    Menu exibido para usuários do tipo cliente.
    """
    print("\n1 - Atualizar minha senha")
    print("2 - Gerenciar produtos")
    print("0 - Logout")

    return Prompt.ask("Escolha uma opção", choices=["0", "1", "2"])


def menu_produtos():
    """
    Menu de operações com produtos.
    """
    print("\n1 - Cadastrar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Buscar produto por ID")
    print("5 - Listar produtos por nome")
    print("6 - Listar produtos por preço")
    print("0 - Voltar")

    return Prompt.ask("Escolha uma opção", choices=["0", "1", "2", "3", "4", "5", "6"])


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def main():
    """
    Executa o sistema inteiro.
    Aqui ficam os laços e a tomada de decisão do programa.
    """
    usuarios = carregar_usuarios(ARQUIVO_USUARIOS)
    produtos = carregar_produtos(ARQUIVO_PRODUTOS)

    usuario_logado = None

    while True:
        # Se ninguém estiver logado, mostra o menu inicial
        if usuario_logado is None:
            opcao = menu_inicial()

            if opcao == "1":
                usuario_logado = fazer_login(usuarios)

            elif opcao == "2":
                cadastrar_usuario(usuarios, usuario_logado)

            elif opcao == "3":
                console.print("[cyan]Encerrando o sistema...[/cyan]")
                break

        # Se houver alguém logado, mostra o menu interno
        else:
            if usuario_logado.tipo == "admin":
                opcao = menu_admin()

                if opcao == "1":
                    atualizar_senha(usuarios, usuario_logado)

                elif opcao == "2":
                    excluir_usuario(usuarios, usuario_logado)

                elif opcao == "3":
                    # Loop específico para o menu de produtos
                    while True:
                        opcao_prod = menu_produtos()

                        if opcao_prod == "1":
                            cadastrar_produto(produtos)

                        elif opcao_prod == "2":
                            atualizar_produto(produtos)

                        elif opcao_prod == "3":
                            excluir_produto(produtos)

                        elif opcao_prod == "4":
                            buscar_produto_por_id(produtos)

                        elif opcao_prod == "5":
                            listar_produtos_ordenados_nome(produtos)

                        elif opcao_prod == "6":
                            listar_produtos_ordenados_preco(produtos)

                        elif opcao_prod == "0":
                            break

                elif opcao == "0":
                    usuario_logado = None
                    console.print("[cyan]Logout realizado.[/cyan]")

            else:
                opcao = menu_cliente()

                if opcao == "1":
                    atualizar_senha(usuarios, usuario_logado)

                elif opcao == "2":
                    # Cliente também pode acessar o menu de produtos
                    while True:
                        opcao_prod = menu_produtos()

                        if opcao_prod == "1":
                            cadastrar_produto(produtos)

                        elif opcao_prod == "2":
                            atualizar_produto(produtos)

                        elif opcao_prod == "3":
                            excluir_produto(produtos)

                        elif opcao_prod == "4":
                            buscar_produto_por_id(produtos)

                        elif opcao_prod == "5":
                            listar_produtos_ordenados_nome(produtos)

                        elif opcao_prod == "6":
                            listar_produtos_ordenados_preco(produtos)

                        elif opcao_prod == "0":
                            break

                elif opcao == "0":
                    usuario_logado = None
                    console.print("[cyan]Logout realizado.[/cyan]")


# ==========================================================
# EXECUÇÃO DO PROGRAMA
# ==========================================================

if __name__ == "__main__":
    main()
