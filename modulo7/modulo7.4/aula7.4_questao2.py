# Importa a biblioteca pathlib
# Ela ajuda a trabalhar com arquivos e pastas
from pathlib import Path

# Importa a biblioteca re
# Ela ajuda a encontrar as palavras dentro do texto
import re


# Descobre a pasta onde este arquivo Python está salvo
pasta_do_script = Path(__file__).resolve().parent


# Cria o caminho do arquivo que já existe
# Este é o arquivo criado no exercício anterior
caminho_frase = pasta_do_script / "frase.txt"


# Cria o caminho do novo arquivo
# É nele que vamos salvar as palavras
caminho_palavras = pasta_do_script / "palavras.txt"


# Abre o arquivo frase.txt para ler
# "r" significa ler
with open(caminho_frase, "r", encoding="utf-8") as arquivo:

    # Lê todo o conteúdo do arquivo
    frase = arquivo.read()


# Procura somente as palavras dentro da frase
# Espaços, vírgulas, pontos e outros sinais são ignorados
palavras = re.findall(r"[^\W\d_]+", frase, flags=re.UNICODE)


# Abre o arquivo palavras.txt para escrever
# "w" significa escrever
with open(caminho_palavras, "w", encoding="utf-8") as arquivo:

    # Percorre cada palavra encontrada
    for palavra in palavras:

        # Escreve uma palavra e pula para a próxima linha
        arquivo.write(palavra + "\n")


# Abre o arquivo palavras.txt para ler o que foi salvo
with open(caminho_palavras, "r", encoding="utf-8") as arquivo:

    # Guarda todo o conteúdo do arquivo
    conteudo = arquivo.read()


# Mostra o conteúdo do arquivo na tela
print(conteudo)
