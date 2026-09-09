# Listas originais
lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]

# Cria uma cópia da primeira lista
diferenca = lista1.copy()

# Percorre cada elemento da segunda lista
for elemento in lista2:
    # Se o elemento ainda estiver na lista diferença,
    # remove apenas uma ocorrência dele
    if elemento in diferenca:
        diferenca.remove(elemento)

print("Listas originais:")
print(lista1)
print(lista2)

print("Diferença entre as listas:")
print(diferenca)
