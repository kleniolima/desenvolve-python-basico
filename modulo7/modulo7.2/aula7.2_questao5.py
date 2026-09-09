# importa a biblioteca randon para misturar as letras
import random

# cria uma função chamada embaralhar_palavras
# a função recebe uma frase 
def embaralhar_palavras(frase):

    # separa a frase em uma lista de palavras
    # exmplo " Python é uma linguagem" vira ["python", "é", "uma", "linguagem"]
    palavras = frase.split()

    # cria uma lista vazia para guardar as palavras modificadas
    palavras_embaralhadas = []

    # percorre cada palavra da lista 
    for palavra in palavras:

        # palavras com 3 letras ou menos n tem letra suficientes 
        if len(palavra) <= 3:

            # mantém a palavra do jeito q esta
            palavras_embaralhadas.append(palavra)

        else:

            # guarda o primeiro carctere da palavra
            primeiro_caractere = palavra[0]

            # guarda o ultimo caractere da palavra
            ultimo_caractere = palavra[-1]

            # pega somente as letras q ficam no meio
            # exemplo
            # "Python"
            # primeiro : "P"
            # meio: "ytho"
            # ultimo: "u"
            letras_do_meio = list(palavra[1:-1])

            # embaralha as letras do meio 
            random.shuffle(letras_do_meio)

            # junta novamente as letras embaralhadas
            meio_embaralhado = "".join(letras_do_meio)

            # monta a palavra completa
            nova_palavra = (
                primeiro_caractere
                + meio_embaralhado
                + ultimo_caractere
            )

            # coloca a nova palavra na lista
            palavras_embaralhadas.append(nova_palavra)

    # junta todas as palavras novamente, colocando espaços entre elas 
    nova_frase = " ".join(palavras_embaralhadas)

    # entrega a frase pronta 
    return nova_frase

# cria uma frase para testar a função 
frase = "python é uma linguagem de programação"

# chama a função e guarda o resultado 
resultado = embaralhar_palavras(frase)

# mostra a frase com as letras internas embaralhadas
print(resultado)