# Cria uma função que recebe um número inteiro
def soma_digitos(numero):

    # Guarda o valor original para verificar se ele é zero
    numero_original = numero

    # Garante que números negativos também possam ser calculados
    numero = abs(numero)

    # Começa a soma com zero
    soma = 0

    # Repete enquanto ainda houver dígitos no número
    while numero > 0:

        # Pega o último dígito do número
        digito = numero % 10

        # Adiciona esse dígito à soma
        soma = soma + digito

        # Remove o último dígito do número
        numero = numero // 10

    # Se o usuário digitou zero, a soma também será zero
    return soma


# Pede um número inteiro ao usuário
numero_usuario = int(input("Digite um número inteiro: "))


# Chama a função para somar os dígitos
resultado = soma_digitos(numero_usuario)


# Mostra o resultado
print(f"A soma dos dígitos é: {resultado}")
