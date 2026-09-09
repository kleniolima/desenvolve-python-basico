# Pede uma frase ao usuário
frase = input("Digite uma frase: ")

# Transforma a frase em letras minúsculas
# Assim, 'A' e 'a' serão considerados a mesma vogal
frase_minuscula = frase.lower()

# Cria uma lista vazia para guardar os índices das vogais
indices_vogais = []

# Verifica cada letra da frase
# enumerate fornece o índice e o caractere
for indice, letra in enumerate(frase_minuscula):

    # Verifica se a letra é uma vogal
    if letra in "aeiou":

        # Guarda o índice da vogal na lista
        indices_vogais.append(indice)

# Mostra a quantidade de vogais
print(len(indices_vogais), "vogais")

# Mostra os índices onde as vogais foram encontradas
print("Índices:", indices_vogais)
