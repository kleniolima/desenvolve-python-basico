# define uma função (def) que recebe uma string chamada texto 
def contagem_caracteres(texto):
    # cria um {}dicionario{} vazio para armazenar os caracteres e as quantidade
    contagens = {}

    # percorre cada caractere existente na string 
    for caractere in texto:
        # verifica se o caractere esta no dicionario
        if caractere in contagens:
            #aumenta em 1 a quantidade do caractere encontrado novamente
            contagens[caractere] += 1
        else:#se nao
            # adciona o caractere ao dicionario com a qtd inicial 1
            contagens[caractere] = 1

    # retorna o dicionario com a contagem dos caracteres.
    return contagens

# armazena a frase que sera analisada 
frase = " python programming"

# chama a função e guarda o dicionario retornado
resultado =  contagem_caracteres(frase)

# exibe o resultado na tela 
print(resultado)