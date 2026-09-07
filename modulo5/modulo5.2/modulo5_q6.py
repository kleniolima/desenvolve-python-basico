# Cria uma função lambda para verificar se o número é par ou ímpar
verificar_paridade = lambda numero: "par" if numero % 2 == 0 else "ímpar"


# Exibe uma mensagem para o usuário
print("digita um numero q eu te falo se é par ou impar")
print("(digite 0 para finalizar o programa):")


# Repete o processo até que o usuário digite 0
while True:
    # Solicita um número e converte o valor para inteiro
    numero = int(input())

    # Verifica se o usuário digitou 0
    if numero == 0:
        # Encerra o laço de repetição
        break

    # Chama a função lambda para verificar a paridade
    resultado = verificar_paridade(numero)

    # Exibe se o número é par ou ímpar
    print(resultado)
