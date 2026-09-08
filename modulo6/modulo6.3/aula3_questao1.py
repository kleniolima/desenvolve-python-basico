numeros = []

print("Digite números inteiros.")
print("Digite 'fim' quando terminar.")
print("Informe pelo menos 4 números.")

while True:
    entrada = input("Número: ")

    if entrada.lower() == "fim":
        if len(numeros) >= 4:
            break
        print("Você precisa digitar pelo menos 4 números.")
        continue

    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'fim'.")

print("\nLista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Índices pares:", numeros[::2])
print("Índices ímpares:", numeros[1::2])
