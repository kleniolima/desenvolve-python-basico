# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Cria uma lista contendo somente as vogais da frase
# lower() transforma a letra em minúscula
# sorted() ordena as vogais em ordem alfabética
vogais = sorted([
    caractere.lower()
    for caractere in frase
    if caractere.lower() in "aeiou"
])

# Cria uma lista contendo somente as consoantes
# isalpha() verifica se o caractere é uma letra
# Espaços, números e pontuações não são adicionados
# A segunda condição remove as vogais
consoantes = [
    caractere
    for caractere in frase
    if caractere.isalpha() and caractere.lower() not in "aeiou"
]

# Imprime a lista de vogais
print("Vogais:", vogais)

# Imprime a lista de consoantes
print("Consoantes:", consoantes)
