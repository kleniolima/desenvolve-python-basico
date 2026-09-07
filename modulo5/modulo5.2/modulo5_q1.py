# Cria uma função chamada fatorial que recebe um número n
def fatorial(n):

    # Começa o resultado com 1
    resultado = 1

    # Repete a operação de 1 até o número informado
    for fator in range(1, n + 1):

        # Multiplica o resultado pelo número atual
        resultado = resultado * fator

    # Devolve o resultado final da função
    return resultado


# Pede ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))


# Chama a função fatorial usando o número informado
resultado = fatorial(numero)


# Exibe o resultado na tela
print(f"O fatorial de {numero} é {resultado}")
