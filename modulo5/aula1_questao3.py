import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Começa o loop para pedir palpites
while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    # Verifica se o palpite está abaixo do número secreto
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")

    # Verifica se o palpite está acima do número secreto
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")

    # Se não é baixo nem alto, o palpite está correto
    else:
        print("Parabéns! Você acertou!")
        break
