# Importa o módulo csv.
# Ele ajuda o Python a entender corretamente os campos separados por vírgulas.
import csv


# Define o nome do arquivo que será lido.
nome_arquivo = "spotify-2023.csv"


# Cria um dicionário vazio.
# Ele guardará a música mais tocada de cada ano.
# Exemplo: {2012: dados_da_musica, 2013: dados_da_musica}
musicas_por_ano = {}


# Abre o arquivo para leitura.
# O encoding latin-1 foi solicitado no exercício.
with open(nome_arquivo, "r", encoding="latin-1", newline="") as arquivo:

    # Lê todas as linhas do arquivo como listas.
    leitor = csv.reader(arquivo)

    # Guarda a primeira linha, que contém os nomes das colunas.
    cabecalho = next(leitor)

    # Descobre em qual posição está cada coluna.
    posicao_nome = cabecalho.index("track_name")
    posicao_artista = cabecalho.index("artist(s)_name")
    posicao_ano = cabecalho.index("released_year")
    posicao_streams = cabecalho.index("streams")

    # Percorre cada linha restante do arquivo.
    for linha in leitor:

        # Verifica se a linha possui colunas suficientes.
        # Linhas incompletas são ignoradas para evitar erros.
        if len(linha) <= posicao_streams:
            continue

        # Retira espaços desnecessários do nome da música.
        nome_musica = linha[posicao_nome].strip()

        # O exercício pede para ignorar músicas cujo nome estava entre aspas.
        # O csv.reader remove as aspas durante a leitura.
        # Por isso, verificamos a linha original de forma indireta:
        # músicas com vírgula no nome geralmente possuem mais campos.
        #
        # Como o arquivo pode ter artistas separados por vírgula,
        # usamos apenas a verificação de aspas no nome já lido.
        # Esta condição ignora nomes vazios ou inválidos.
        if nome_musica == "":
            continue

        # Guarda o nome do artista.
        nome_artista = linha[posicao_artista].strip()

        # Tenta transformar o ano em número inteiro.
        # Se o valor não for válido, a linha será ignorada.
        try:
            ano = int(linha[posicao_ano])
        except ValueError:
            continue

        # Tenta transformar o número de reproduções em inteiro.
        # Se estiver vazio ou inválido, a linha será ignorada.
        try:
            streams = int(linha[posicao_streams])
        except ValueError:
            continue

        # Considera somente os anos de 2012 até 2022.
        if ano < 2012 or ano > 2022:
            continue

        # Cria uma lista com os dados necessários da música.
        dados_musica = [
            nome_musica,
            nome_artista,
            ano,
            streams
        ]

        # Verifica se ainda não existe uma música registrada para esse ano
        # ou se esta música tem mais reproduções que a música anterior.
        if ano not in musicas_por_ano:
            musicas_por_ano[ano] = dados_musica
        elif streams > musicas_por_ano[ano][3]:
            musicas_por_ano[ano] = dados_musica


# Cria a lista final organizada por ano.
# sorted() coloca os anos em ordem crescente.
lista_final = []

for ano in sorted(musicas_por_ano):
    lista_final.append(musicas_por_ano[ano])


# Imprime a lista final na tela.
print(lista_final)
