import random

lista1 = []
lista2 = []

# Preenche as duas listas com 20 valores aleatórios
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

# Cria a lista de intersecção sem valores duplicados
interseccao = []

for valor in lista1:
    if valor in lista2 and valor not in interseccao:
        interseccao.append(valor)

# Ordena a lista de intersecção
interseccao.sort()

# Imprime as listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Intersecção ordenada:", interseccao)

# Imprime a quantidade de vezes que cada elemento aparece
print("\nContagem:")

for valor in interseccao:
    quantidade_lista1 = lista1.count(valor)
    quantidade_lista2 = lista2.count(valor)

    print(
        valor,
        ": (lista1 =", quantidade_lista1,
        ", lista2 =", quantidade_lista2, ")"
    )
