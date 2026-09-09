# solicira ao user q digite a frase
frase = input("digite 1 frase: ")

#define as vogais que serao substituidas
#INCLUI MAIUSCULAS E MINUSCULAS
vogais = "aeiouAEIOU"

# cria 1 variavel vazia para armazenar a frase modificada
frase_modificada = ""

#percorre cada caractere da frase digitada
for caractere in frase:

     # verifica se o caractere é uma vogal 
     if caractere in vogais:

          # se for vogal pai, adciona "*" à nova frase 
          frase_modificada += "*"

     else:

          # se nao for uma vogal, mantem o caractere original
          frase_modificada += caractere

# exibe a frase dps da substuiçãod das vogais 
print("frase modificada:", frase_modificada)