lista1 = []
lista2 = []

# Lê a quantidade de elementos da primeira lista
quantidade1 = int(input("Digite a quantidade de elementos da lista 1: "))

print(f"\nDigite os {quantidade1} elementos da lista 1:")

for i in range(quantidade1):
    valor = int(input())
    lista1.append(valor)

# Lê a quantidade de elementos da segunda lista
quantidade2 = int(input("\nDigite a quantidade de elementos da lista 2: "))

print(f"\nDigite os {quantidade2} elementos da lista 2:")

for i in range(quantidade2):
    valor = int(input())
    lista2.append(valor)

# Cria a lista intercalada
lista_intercalada = []

menor_quantidade = min(quantidade1, quantidade2)

# Intercala os elementos enquanto as duas listas têm valores
for i in range(menor_quantidade):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adiciona os elementos restantes da lista maior
if quantidade1 > quantidade2:
    for i in range(menor_quantidade, quantidade1):
        lista_intercalada.append(lista1[i])
else:
    for i in range(menor_quantidade, quantidade2):
        lista_intercalada.append(lista2[i])

print("\nLista intercalada:", *lista_intercalada)
