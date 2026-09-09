# Pede o número de celular ao usuário
numero = input("Digite o número: ")

# Verifica se o número tem 8 dígitos
if len(numero) == 8:
    # Acrescenta o número 9 no começo
    numero = "9" + numero

# Verifica se o número tem 9 dígitos
if len(numero) == 9:

    # Confere se o primeiro dígito é 9
    if numero[0] == "9":

        # Separa o número no formato 5-4
        numero_formatado = numero[:5] + "-" + numero[5:]

        # Mostra o número completo
        print("Número completo:", numero_formatado)

    else:
        print("Número inválido: o primeiro dígito deve ser 9.")

else:
    print("Número inválido: digite 8 ou 9 dígitos.")
