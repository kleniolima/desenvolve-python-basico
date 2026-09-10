# define uma função que verifica se uma frase é panagrama 
def checa_panagrama(frase):
    # cria 1 conjunto com tds as letras do alfabeto
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")

    # converte a frase para letras minusculas
    # depois, transforma a frase em um conjunto de caracteres unicos 
    letras_da_frase = set(frase.lower())

    # verifica se todas as letas do alfabeto aparecem na frase 
    return alfabeto <= letras_da_frase

# define uma frase que possui todas as letras do alfabeto 
frase1 = "the quick brown fox jumps over the lazy dog"

# chama a funcao q verifica a primeira frase 
resultado1 = checa_panagrama(frase1)

# mostra o resultado da primeira frase
if resultado1:
    print("É um Panagrama")
else:
    print("Não é um Panagrama")


# define uma frase q nao possui todas as letras do alfabeto
frase2 = "Python é uma linguagem de programação"

# chama a função para verificar a segunda frase 
resultado2 = checa_panagrama(frase2)

# mostra o resultado da segunda frase 
if resultado2:
    print("è um panagrama")
else:
    print("nao é um Panagrama")