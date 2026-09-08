import random

# Gera uma lista com 20 valores inteiros entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Cria uma nova lista ordenada, sem modificar a original
lista_ordenada = sorted(lista)

# Obtém os índices do maior e do menor valor
indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

# Imprime na ordem solicitada
print("Lista ordenada:", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
