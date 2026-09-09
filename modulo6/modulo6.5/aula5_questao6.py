import random

# Cria uma lista com 20 números aleatórios entre 1 e 100
lista = [random.randint(1, 100) for i in range(20)]

# Imprime a lista original
print("Lista original:")
print(lista)

# Continua executando até o usuário digitar 0
while True:
    tamanho = int(input("\nTamanho para divisão: "))

    # Encerra o programa quando o tamanho informado for 0
    if tamanho == 0:
        print("Programa encerrado.")
        break

    # Evita valores negativos ou inválidos
    if tamanho < 0:
        print("Digite um tamanho positivo ou 0 para sair.")
        continue

    # Cria sublistas usando fatias da lista original
    sublistas = [
        lista[inicio:inicio + tamanho]
        for inicio in range(0, len(lista), tamanho)
    ]

    # Exibe as sublistas
    print("Sublistas:")
    print(sublistas)
