import random


def encrypt(nomes):
    # Sorteia um número entre 1 e 10.
    # Esse número será a chave da criptografia.
    chave = random.randint(1, 10)

    # Aqui vamos guardar os nomes depois da criptografia
    nomes_criptografados = []

    # Pega um nome de cada vez
    for nome in nomes:

        # Começamos com um nome vazio.
        # Aos poucos, vamos colocando as letras criptografadas nele.
        novo_nome = ""

        # Pega uma letra de cada vez do nome
        for letra in nome:

            # ord transforma uma letra em um número
            codigo = ord(letra)

            # Avança a letra de acordo com a chave
            novo_codigo = codigo + chave

            # chr transforma o número novamente em uma letra
            nova_letra = chr(novo_codigo)

            # Coloca a nova letra no novo nome
            novo_nome = novo_nome + nova_letra

        # Guarda o nome pronto na lista
        nomes_criptografados.append(novo_nome)

    # Devolve os nomes criptografados e a chave usada
    return nomes_criptografados, chave


# Lista original de 

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Chama a função e guarda as duas respostas
nomes_criptografados, chave_aleatoria = encrypt(nomes)

# Mostra os resultados
print("Nomes criptografados:", nomes_criptografados)
print("Chave:", chave_aleatoria)
