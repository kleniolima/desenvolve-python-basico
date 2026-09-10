# Define uma função que recebe um dicionário
# e uma lista com as chaves que devem ser filtradas.
def filtrar_dicionario(dicionario, chaves_filtradas):
    # Cria um novo dicionário para armazenar apenas
    # as chaves permitidas e seus respectivos valores.
    resultado = {}

    # Percorre cada chave presente na lista de chaves filtradas.
    for chave in chaves_filtradas:
        # Verifica se a chave existe no dicionário original.
        if chave in dicionario:
            # Copia a chave e o valor correspondente
            # para o novo dicionário.
            resultado[chave] = dicionario[chave]

    # Retorna o novo dicionário com os dados filtrados.
    return resultado


# Cria o dicionário que será utilizado como fonte dos dados.
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Cria uma lista contendo as chaves que devem permanecer no resultado.
chaves_filtradas = ['a', 'c', 'e']

# Chama a função e armazena o novo dicionário retornado.
resultado = filtrar_dicionario(dados, chaves_filtradas)

# Exibe o dicionário filtrado na tela.
print(resultado)
