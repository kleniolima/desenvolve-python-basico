# Pede para o usuário digitar uma frase
frase = input("Digite a frase: ").strip()

# Começa o contador em zero
quantidade_espacos = 0

# Passa por cada caractere da frase
for caractere in frase:

    # Verifica se o caractere é um espaço em branco
    if caractere == " ":

        # Adiciona 1 ao contador
        quantidade_espacos = quantidade_espacos + 1

# Mostra a quantidade de espaços encontrados
print("Espaços em branco:", quantidade_espacos)
