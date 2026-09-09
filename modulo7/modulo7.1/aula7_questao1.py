# Pede para o usuário digitar o nome
nome = input("Digite seu nome: ")

# Começa contando apenas 1 letra
# O len(nome) indica quantas letras existem no nome
for quantidade in range(1, len(nome) + 1):

    # Pega somente as primeiras letras do nome
    # Exemplo: nome[:2] pega as 2 primeiras letras
    parte_do_nome = nome[:quantidade]

    # Imprime a parte do nome que foi separada
    print(parte_do_nome)
