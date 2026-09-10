# guarda a frase que sera analisada 
frase = "o rato roeu a roupa da Alice"

# cria uma string contendo TODAS as vogais
# usaremos essa string para verificar cara caractere da frase 
vogais = "aeiou"

# a função enumerate() percorre a frase e fornece:
# o indice do carctere;
# o caractere encontrado nesse indice.
for indice, caractere in enumerate(frase):

    # converte o caractere para letras minusculas
    # isso permite indentificar tanto "A"" quanto "a"
    caractere_minusculo = caractere.lower()

    # verifica se o caractere é uma das vogais 
    if caractere_minusculo in vogais:
        # mostra a vogal encontrada e sua posição na frase 
        print(f"A vogal '{caractere}' aparece no indice {indice} ")