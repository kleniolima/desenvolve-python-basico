# define a primeira lista 
A = [1,4,5,7,9]

#defina a segunda
B = [4,5,7,9]

# converte as listas em conjuntos 
conjunto_A = set(A)
conjunto_B = set(B)

# encontra os elementos que estao em A mas n tao em B 
faltando_na_segunda = conjunto_A - conjunto_B

# econtra os elementos q estao em B mas n tao em A
faltando_na_primeira = conjunto_B - conjunto_A

# verifica se existe algum elemento faltando na segunda lista 
if faltando_na_segunda:
    # pega o unico elemento diferente
    elemento = faltando_na_segunda.pop()

    # mostra q ele esta faltando na segunda lista 
    print(f"o elemento {elemento} está faltando na segunda lista")


# verifica se existe algum elemento faltando na primeira lista
elif faltando_na_primeira:
    # pega o unico elemento diferente
    elemento = faltando_na_primeira.pop()


    # mostra que ele esta faltando na primeira lista 
    print(f"O elemento {elemento} está faltando na primeira lista")

# executa caso nao exista nenhuma diferença
else:
    print("as linhas sao iguais")