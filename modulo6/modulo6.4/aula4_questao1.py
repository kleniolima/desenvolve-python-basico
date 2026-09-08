# Números pares entre 20 e 50, incluindo 20 e 50
pares = [numero for numero in range(20, 51) if numero % 2 == 0]

# Quadrados dos valores de 1 até 9
quadrados = [numero ** 2 for numero in range(1, 10)]

# Números entre 1 e 100 divisíveis por 7
divisiveis_por_7 = [
    numero for numero in range(1, 101)
    if numero % 7 == 0
]

# "par" ou "impar" para cada valor de range(0, 30, 3)
paridade = [
    "par" if numero % 2 == 0 else "impar"
    for numero in range(0, 30, 3)
]

print("Números pares:", pares)
print("Quadrados:", quadrados)
print("Divisíveis por 7:", divisiveis_por_7)
print("Paridade:", paridade)
