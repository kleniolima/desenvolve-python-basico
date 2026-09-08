import random

numeros = []

for _ in range(20):
    numeros.append(random.randint(-10, 10))

print("Original:", numeros)

maior_inicio = 0
maior_fim = 0
inicio_atual = None

for i, numero in enumerate(numeros):
    if numero < 0:
        if inicio_atual is None:
            inicio_atual = i
    else:
        if inicio_atual is not None:
            if i - inicio_atual > maior_fim - maior_inicio:
                maior_inicio = inicio_atual
                maior_fim = i

            inicio_atual = None

# Verifica se a maior sequência termina no último elemento
if inicio_atual is not None:
    if len(numeros) - inicio_atual > maior_fim - maior_inicio:
        maior_inicio = inicio_atual
        maior_fim = len(numeros)

del numeros[maior_inicio:maior_fim]

print("Editada: ", numeros)
