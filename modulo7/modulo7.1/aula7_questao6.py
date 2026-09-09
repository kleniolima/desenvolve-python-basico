# Pede uma frase ao usuário
frase = input("Digite uma frase: ")

# Pede a palavra que será procurada
palavra_objetivo = input("Digite a palavra objetivo: ")

# Cria uma lista vazia para guardar os anagramas
anagramas = []

# Organiza as letras da palavra objetivo em ordem alfabética
objetivo_organizado = sorted(palavra_objetivo.lower())

# Separa a frase em palavras
palavras = frase.split()

# Verifica cada palavra da frase
for palavra in palavras:

    # Organiza as letras da palavra atual
    palavra_organizada = sorted(palavra.lower())

    # Compara as letras da palavra atual com as letras do objetivo
    if palavra_organizada == objetivo_organizado:

        # Guarda a palavra original na lista
        anagramas.append(palavra)

# Mostra os anagramas encontrados
print("Anagramas:", anagramas)
