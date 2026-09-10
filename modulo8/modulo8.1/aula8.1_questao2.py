# define uma função que recebe duas listas 
def tem_elementos_comuns(lista1, lista2):
    # converte a primeira lista em um conjunto 
    conjunto1 = set(lista1)

    # converte a segunda lista em um conjunto 
    conjunto2 = set(lista2)

    # encontra os elementos presentes nos dois conjuntos 
    elementos_comuns = conjunto1 & conjunto2

    # retorna TRUE se houver algum elemento comum
    # e tb retorna false se a interceção estiver vazia 
    return bool(elementos_comuns)

# cria a primeira lista para o teste
lista1 = [1,2,3,4]

# cria a segunda lista para o testt
lista2 = [3,4,5,6,7]

#chama a função e guarda o resultado
resultado = tem_elementos_comuns(lista1=lista1, lista2=lista2)

# mostra o resultaddo
print(resultado)  # saida esperada true