import random

num_elementos = random.randint(5, 20)

elementos = []

for i in range(num_elementos):
    valor = random.randint(1, 10)
    elementos.append(valor)

soma = sum(elementos)
media = soma / num_elementos

print("Elementos:", elementos)
print("Soma:", soma)
print("Média:", media)
