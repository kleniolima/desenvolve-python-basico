# o programa vai continuar fincionando até q o usuario digitar fim
while True:

    # pede  uma frase ao usuario 
    frase = input(
       'Digite uma frase ( digite fim para encerrar): ' 
    )

    # verifica se o usuario digitou "fim"
    # o metodo lower() transforma tudo em letras minusculas
    if frase.lower() == "fim":

        # encerra o laço de repetição
        break

    # cria uma frase vazia para guardar somente letras e numeros
    frase_limpa = ""

    # Percorre cada caractere da frase digitada 
    for caractere in frase:

        # isalnum() verifica se o caractere é uma letra ou um numr
        # assim, espaços e sinais de pontuação sao ignorados
        if caractere.isalnum():

            # Adciona o caractere em letra minuscula 
            frase_limpa += caractere.lower()

    # cria uma versao da frase de traz pra frente 
    frase_invertida = frase_limpa[::-1]

    # compara a frase normal com a frase invertida 
    if frase_limpa == frase_invertida:

        # mostra es mensagem quando as duas sao iguais
        print(f'"{frase}" é um palindromo')

    else:

        # mostra essa msg qd as 2 sao diferentes
        print(f'"{frase}" não é palíndromo')