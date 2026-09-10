# define uma função que recebe dois dicionarios
def mesclar_dicionarios(dicionario1, dicionario2):
    # cria um novo dicionario com os dados do primeiro dicionario
    resultado = dicionario1.copy()

    # percorre cada chave e valor do segundo dicionario 
    for chave , valor in dicionario2.items():
        # verifica se a chave ja existe no dicionario resultante
        if chave in resultado:
            # mantem o maior valor entre dois dicionarios
            resultado[chave] = max(resultado[chave], valor)
        else:
            # adciona a chave quando ela ainda nao existe
            resultado[chave] = valor

    # retorna o novo dicionario mesclado 
    return resultado

# cria o primeiro dicionario 
dicionario1 = {'a': 1, 'b': 2, 'c': 3}

# cria o segundo dicionario 
dicionario2 = {'b': 4, 'd': 5}

# chama a função e guarda o dicionario resultante
resultado = mesclar_dicionarios(dicionario1=dicionario1, dicionario2=dicionario2)

# exibe o resultado na tela 
print(resultado)