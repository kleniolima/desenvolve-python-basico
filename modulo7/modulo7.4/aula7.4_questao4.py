# importa a biblioteca pathlib
# ela ajuda a encontrar os arquivos
from pathlib import Path


# importa a biblioteca random
# ela serve pra deixar aleatorio as paradinha
import random

# importa a biblioteca " re "
# ajuda a separar os desenhos do enforcado 
import re


# descobre a pasta onde este programa esta salvo
pasta_do_script = Path(__file__).resolve().parent

#cria o caminho do arquivo com os desenhos 
caminho_do_enforcado = pasta_do_script / "gabarito_enforcado.txt"

# caminho do aquivo das palavras
caminho_das_palavras = pasta_do_script / "gabarito_forca.txt"

# abre o arquivo das palavras para leitura
with open(caminho_das_palavras, "r", encoding="utf-8") as arquivo:

    # lê todas as linhas do arquivo
    linhas = arquivo.readlines()


# remove espaços e quebras de linha
# tb ignora linhas vazias
palavras = [
    linha.strip().upper()
    for linha in linhas
    if linha.strip()
]


# escolhe uma palavra aleatoriamente
palavra = random.choice(palavras)

# abre o arquivo com os desenhos do enforcado
with open(caminho_do_enforcado, "r", encoding="utf-8") as arquivo:


    # le todo o conteudo do arquivo
    texto_enforcado = arquivo.read()

# separa os desenhos pelas linhas vazias
estagios_enforcado = re.split(
    r"\n\s*\n",
    texto_enforcado.strip()
)

# cria uma lista com underline para cada letra 
progresso = ["_"] * len(palavra)

# guarda as letras que ja foram digitadas
letras_digitadas = set()


# começa com zero erros
quantidade_erros = 0 

# cria a função que mostra o desenho do enforcado
# recebe o numero de erros do jogador 
def imprime_enforcado(numero_de_erros):

    # mostra o desenho correspondente ao numero de erros
    print(estagios_enforcado[numero_de_erros])

# mostra o título do jogo
print("Jogo da Forca criado por Klenio")
print("-------------")

# mostra o primeiro desenho, antes de qualquer erro
imprime_enforcado(0)

# mostra a quantidade de letras da palavra
print(f"A palavra tem {len(palavra)} letras.")


# mostra um underline para cada letra 
print (" ".join(progresso))

# repete eqt o jogador tiver menos de 6 erros
# e ainda nao tiver descoberto a palavra 
while quantidade_erros < 6 and "_" in progresso:

    # oede uma letra ao jogador
    letra = input("\nDigite uma letra: ").strip().upper()


    # verifica se foi digitada somente uma letra
    if len(letra) != 1 or not letra.isalpha():

        print("Digite apenas uma letra.")
        continue


    # verifica se a letra ja foi usada 
    if letra in letras_digitadas:

        print("Voce já digitou essa letra.")
        continue

    # guarda a letra digitada
    letras_digitadas.add(letra)


    # verifica se a letra está na palavra 
    if letra in palavra:

        print("Voce acertou!")

        # procura a letra em cada posição da palavra
        for posicao in range(len(palavra)):

            # verifica se a letra está nessa posição 
            if palavra[posicao] == letra:
                progresso[posicao] = letra
 
    else:
  
        print("voce errou!")

        # aumenta a quantidade de erros
        quantidade_erros += 1
 
        # mostra o desenho correspondente ao erro
        imprime_enforcado(quantidade_erros)

        # mostra o progresso depois de cada tentativa
    print("\nPalavra:")
    print(" ".join(progresso))


# mostra o progresso atual da palavra 
print("\nPalavra:")
print(" ".join(progresso))

# verifica se nao existem mais underscores
if "_" not in progresso:
    # mostra msg de vitória 
    print("\nParabens! voce ganhou !")
    print(f"A palavra era: {palavra}")


else:
    # mostra a msg de derrota 
    print("\nVc Perdeu!")
    print(f"A palavra era: {palavra}")