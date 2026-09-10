# Define a função que recebe uma lista de tuplas
def comprimir_tuplas(tuplas):
    # Cria um dicionário vazio
    # Ele guardará cada palavra e a soma dos seus números
    palavras_somadas = {}

    # Percorre cada tupla da lista
    for palavra, numero in tuplas:

        # Verifica se a palavra já foi encontrada antes
        if palavra in palavras_somadas:

            # Se a palavra já existe, soma o novo número
            palavras_somadas[palavra] = palavras_somadas[palavra] + numero

        else:

            # Se a palavra ainda não existe, adiciona-a ao dicionário
            palavras_somadas[palavra] = numero

    # Converte o dicionário em uma lista de tuplas
    return list(palavras_somadas.items())


# Cria a lista original
tuplas_originais = [
    ('maçã', 3),
    ('banana', 2),
    ('maçã', 5),
    ('laranja', 1),
    ('banana', 3)
]

# Chama a função
resultado = comprimir_tuplas(tuplas_originais)

# Mostra o resultado
print(resultado)
