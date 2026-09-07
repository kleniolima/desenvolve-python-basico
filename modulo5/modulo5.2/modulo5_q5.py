# Importa a biblioteca math para usar o valor de pi
import math


# Função que calcula o perímetro de um triângulo
def calcula_perimetro_triangulo(lado1, lado2, lado3):
    # O perímetro do triângulo é a soma dos três lados
    return lado1 + lado2 + lado3


# Função que calcula o perímetro de um círculo
def calcula_perimetro_circulo(raio):
    # O perímetro do círculo é calculado pela fórmula 2 * pi * raio
    return 2 * math.pi * raio


# Função que calcula o perímetro de um retângulo ou quadrado
def calcula_perimetro_retangulo(lado1, lado2=None):
    # Se lado2 não for informado, significa que a figura é um quadrado
    if lado2 is None:
        # O perímetro do quadrado é quatro vezes o tamanho do lado
        return 4 * lado1

    # Caso lado2 seja informado, calcula o perímetro do retângulo
    return 2 * (lado1 + lado2)


# Repete o programa até que o usuário escolha a opção "Sair"
while True:
    # Exibe o menu de opções
    print("\n1 - Calcular perímetro triângulo")
    print("2 - Calcular perímetro círculo")
    print("3 - Calcular perímetro retângulo")
    print("4 - Sair")

    # Solicita ao usuário uma opção e converte o valor para inteiro
    opcao = int(input("\nOpção: "))

    # Verifica se o usuário escolheu calcular o perímetro do triângulo
    if opcao == 1:
        # Solicita os três lados do triângulo
        print("Digite os três lados do triângulo:")
        lado1 = int(input())
        lado2 = int(input())
        lado3 = int(input())

        # Chama a função responsável pelo cálculo do triângulo
        perimetro = calcula_perimetro_triangulo(lado1, lado2, lado3)

        # Exibe o resultado na tela
        print("O perímetro é:", perimetro)

    # Verifica se o usuário escolheu calcular o perímetro do círculo
    elif opcao == 2:
        # Solicita o raio do círculo
        raio = int(input("Digite o raio do círculo: "))

        # Chama a função responsável pelo cálculo do círculo
        perimetro = calcula_perimetro_circulo(raio)

        # Exibe o resultado na tela
        print("O perímetro é:", perimetro)

    # Verifica se o usuário escolheu calcular o perímetro do retângulo
    elif opcao == 3:
        # Solicita os lados do retângulo
        print("Informe os dois lados do retângulo.")
        print("Se for um quadrado, digite 0 para o segundo valor:")

        lado1 = int(input())
        lado2 = int(input())

        # Se o segundo lado for zero, considera que a figura é um quadrado
        if lado2 == 0:
            # Chama a função informando apenas o primeiro lado
            perimetro = calcula_perimetro_retangulo(lado1)

        # Caso contrário, considera que a figura é um retângulo
        else:
            # Chama a função informando os dois lados
            perimetro = calcula_perimetro_retangulo(lado1, lado2)

        # Exibe o resultado na tela
        print("O perímetro é:", perimetro)

    # Verifica se o usuário escolheu sair do programa
    elif opcao == 4:
        # Exibe uma mensagem de encerramento
        print("Programa encerrado.")

        # Interrompe o laço de repetição
        break

    # Caso o usuário digite uma opção que não existe
    else:
        # Informa que a opção escolhida é inválida
        print("Opção inválida.")
