# Função que inverte os algarismos de um número
def inverterValor(numero):

    # Guarda o sinal do número, caso ele seja negativo
    sinal = 1

    if numero < 0:
        sinal = -1
        numero = abs(numero)

    # Começa o número invertido com zero
    invertido = 0

    # Repete enquanto ainda existirem algarismos
    while numero > 0:

        # Pega o último algarismo do número
        algarismo = numero % 10

        # Coloca o algarismo no número invertido
        invertido = invertido * 10 + algarismo

        # Remove o último algarismo do número original
        numero = numero // 10

    # Retorna o número invertido com o sinal original
    return sinal * invertido


# Função que verifica o número original e o número invertido
def verificarInverso(original, invertido):

    # Verifica se os dois números são iguais
    sao_iguais = original == invertido

    # Verifica se os dois números são ímpares
    ambos_impares = original % 2 != 0 and invertido % 2 != 0

    # Retorna True se uma das condições for verdadeira
    return sao_iguais or ambos_impares


# Pede um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))


# Inverte o número usando a primeira função
numero_invertido = inverterValor(numero)


# Verifica o número original e o invertido
resultado_verificacao = verificarInverso(numero, numero_invertido)


# Mostra o número invertido
print(f"Valor invertido: {numero_invertido}")

# Mostra o resultado da verificação
print(f"Verificação: {resultado_verificacao}")
