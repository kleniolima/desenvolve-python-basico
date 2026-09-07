# Pergunta ao usuário qual operação deseja realizar
print("Opções: (1) maior ou (2) menor?")
opcao = int(input("Opção: "))


# Cria uma lista para armazenar os valores digitados
valores = []

# Solicita os valores ao usuário
print("\nDigite os valores de entrada.")
print("Digite 0 para finalizar a entrada de valores.")


# Continua solicitando valores até o usuário digitar 0
while True:
    # Lê um valor inteiro
    valor = int(input())

    # Verifica se o valor digitado é 0
    if valor == 0:
        # Encerra a entrada de valores
        break

    # Adiciona o valor à lista
    valores.append(valor)


# Verifica se o usuário escolheu a opção "maior"
if opcao == 1:
    # Cria uma função lambda que retorna o maior valor da lista
    calcular = lambda lista: max(lista)

    # Executa a função lambda
    resultado = calcular(valores)

    # Exibe o maior valor
    print("O maior valor é:", resultado)


# Verifica se o usuário escolheu a opção "menor"
elif opcao == 2:
    # Cria uma função lambda que retorna o menor valor da lista
    calcular = lambda lista: min(lista)

    # Executa a função lambda
    resultado = calcular(valores)

    # Exibe o menor valor
    print("O menor valor é:", resultado)


# Caso o usuário escolha uma opção inexistente
else:
    print("Opção inválida.")
