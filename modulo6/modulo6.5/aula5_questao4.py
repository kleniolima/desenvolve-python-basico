n = int(input("Digite n: "))

matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        linha.append(i * j)

    matriz.append(linha)

print("Matriz:")
print(matriz)
