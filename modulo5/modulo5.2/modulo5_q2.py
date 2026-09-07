# Cria uma função que recebe dois números
def soma_quadrados(numero1, numero2):

    # Calcula o quadrado do primeiro número
    quadrado1 = numero1 ** 2

    # Calcula o quadrado do segundo número
    quadrado2 = numero2 ** 2

    # Soma os dois quadrados e retorna o resultado
    return quadrado1 + quadrado2


# Pede o primeiro número ao usuário
primeiro_numero = float(input("Digite o primeiro número: "))

# Pede o segundo número ao usuário
segundo_numero = float(input("Digite o segundo número: "))


# Chama a função usando os dois números informados
resultado = soma_quadrados(primeiro_numero, segundo_numero)


# Mostra o resultado na tela
print(f"A soma dos quadrados é: {resultado}")
