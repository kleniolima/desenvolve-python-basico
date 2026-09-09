# pede o CPF ao usuario 
cpf = input("Digite o CPF (XXX.XXX.XXX-xx): ")

# Remove os pontos e o traço do CPF 
# Exemplo:
# 111.444.777-35 vira 11144477735
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

# Verifica se o Cpf possui exatamente 11 numeros
if len(cpf) != 11 or not cpf.isdigit():
    print("Inválido")

else:
    # Separa os 9 primeiros números do CPF
    primeiros_nove = cpf[:9]

    # -------------------------------
    # Cálculo do primeiro digito 
    # -------------------------------

    soma = 0 

    # Os multiplicadores do primeiro cálculo são:
    # 10, 9, 8, 7, 6, 5, 4, 3, 2
    for i in range(9):
        numero = int(primeiros_nove[i])
        multiplicador = 10 - i

        soma = soma + numero * multiplicador 

    resto = soma % 11

    # Se o resto for 0 ou 1, o dígito será 0
    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    #---------------------------------
    # Cálculo do segundo digito
    #---------------------------------

    # Agora usamos os 9 primeiros numeros 
    # junto com o  primeiro digitoo calculado
    dez_numeros = primeiros_nove + str(primeiro_digito)

    soma = 0 

    # os multiplicadores agora sao:
    # 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
    for i in range(10):
        numero = int(dez_numeros[i])
        multiplicador = 11 - i

        soma = soma + numero * multiplicador

    resto = soma % 11

    #calcula o segundo digito 
    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    # Junta os dois dígitos calculados
    digitos_calculados = str(primeiro_digito) + str(segundo_digito)

    # pega os dois digitos que foram digitados no CPF 
    digitos_digitados = cpf[9:]

    # compara os digitos 
    if digitos_calculados == digitos_digitados:
        print("Válido")
    else:
        print("invalido")