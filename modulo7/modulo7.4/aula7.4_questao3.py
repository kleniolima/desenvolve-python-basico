# importa a biblioteca pathlib
# ela ajuda a encontrar o local dos arquivos
from pathlib import Path


# importa a biblioteca re 
# ela ajuda a procurar palavras especificas no texto
import re


# descobre a pasta onde este programa Python esta salvo
pasta_do_script = Path(__file__).resolve().parent

# cria o caminho completo do arquivo estomago.txt
# o arquivo precisa estar na mesma pasta desde programa
caminho_do_arquivo = pasta_do_script / "estomago.txt"


# abre o arquivo para leitura
# "r" significa read, que quer dizer LER
with open(caminho_do_arquivo, "r", encoding="utf-8") as arquivo:

    #lê todas as linhas e guarda em uma lista
    linhas = arquivo.readlines()


# mostra um titulo para indicar o inicio das 25 primeiras linhas
print("Primeiras 25 linhas")
print("-------------------")

# pega as primeiras 25 linhas do arquivo
# o numero 25 indica quantas linhas queremos mostrar
for linha in linhas[:25]:

    # end="" evita criar uma linha em branco extra 
    # a propria linha já possui uma quebra de linha
    print(linha, end="")


# mostra o numero total de linhas do arquivo
print("\n\nNÙMERO TOTAL DE LINHAS")
print("-----------------------")
print(len(linhas))


# encontra a linha com maior quantidade de caracteres
# a função len conta qts caracteres existem em cada linha
linha_maior = max(linhas, key=len)


# mostra a linha mais comprida 
print("\nLINHA COM MAIOR NUMERO DE CARACTERES")
print("------------------------------------")
print(linha_maior, end="")


# junta todas as linhas em um unico texto
# isso facilita a procura dos nomes 
texto_completo = "".join(linhas)


# procura o nome nonato
# \b significa q estamos procurando a palavra inteira
# re.IGNORACE permite esncotrar nonato, Nonato, NONATO etc.
quantidade_nonato = len(
    re.findall(r"\bNonato\b", texto_completo, flags=re.IGNORECASE)
)

# procura o nome Iria
# o nome precisa aparecer como uma palavra inteira
# re.IGNORECASE ignora diferenças entre maiusculas e minusculas
quantidade_iria = len(
    re.findall(r"\bIria\b", texto_completo, flags=re.IGNORECASE)
)


# soma a quantidade de vezes que cada nome aparecem
quantidade_total = quantidade_nonato + quantidade_iria

# mostra a quantidade de vezes que cada nome apareceu 
print("\n\nMENÇOES AOS PERSONAGENS")
print("----------------------")
print(f"Nonato:  {quantidade_nonato}")
print(f"Iria:  {quantidade_iria}")
print(f"Total:  {quantidade_total}")