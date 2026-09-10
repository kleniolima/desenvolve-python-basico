# Importa o módulo que será usado para encontrar as palavras no texto.
import re


# Abre o arquivo estomago.txt para leitura.
# O arquivo precisa estar na mesma pasta que este programa.
with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    # Lê todo o conteúdo do arquivo.
    texto = arquivo.read()


# Converte todas as letras para minúsculas.
# Assim, "O" e "o" serão consideradas a mesma palavra.
texto = texto.lower()


# Encontra as palavras no texto.
# Os sinais de pontuação, como vírgulas e pontos, não serão incluídos.
palavras = re.findall(r"[a-záàâãéêíóôõúç0-9-]+", texto)


# Cria um dicionário vazio.
# As palavras serão armazenadas como chaves,
# e suas quantidades serão armazenadas como valores.
contagem_palavras = {}


# Percorre todas as palavras encontradas no arquivo.
for palavra in palavras:
    # Verifica se a palavra já foi adicionada ao dicionário.
    if palavra in contagem_palavras:
        # Aumenta em 1 a quantidade da palavra encontrada novamente.
        contagem_palavras[palavra] += 1
    else:
        # Adiciona uma palavra nova com a quantidade inicial de 1.
        contagem_palavras[palavra] = 1


# Organiza os itens do dicionário pela quantidade de ocorrências.
# O segundo elemento de cada item é o número de vezes que a palavra apareceu.
# reverse=True coloca as maiores quantidades primeiro.
itens_ordenados = sorted(
    contagem_palavras.items(),
    key=lambda item: item[1],
    reverse=True
)


# Transforma os itens ordenados novamente em um dicionário.
dicionario_ordenado = dict(itens_ordenados)


# Exibe na tela o dicionário com as palavras mais frequentes no início.
print(dicionario_ordenado)
