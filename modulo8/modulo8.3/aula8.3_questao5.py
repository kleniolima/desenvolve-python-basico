# Define uma função que recebe uma lista de dicionários
# contendo os votos de várias sessões eleitorais.
def resultado_votacao(votos):
    # Cria um dicionário vazio para armazenar
    # o total de votos de cada candidato.
    totais = {}

    # Percorre cada dicionário de votos da lista.
    for sessao in votos:
        # Percorre cada candidato e sua quantidade de votos
        # dentro da sessão atual.
        for candidato, quantidade in sessao.items():
            # Verifica se o candidato já foi registrado.
            if candidato in totais:
                # Soma os votos da sessão atual aos votos anteriores.
                totais[candidato] += quantidade
            else:
                # Registra o candidato com a quantidade inicial de votos.
                totais[candidato] = quantidade

    # Soma os votos de todos os candidatos
    # para descobrir o total geral da votação.
    total_geral = sum(totais.values())

    # Cria um dicionário vazio para armazenar
    # os totais e percentuais finais.
    resultado = {}

    # Verifica se existem votos antes de calcular os percentuais.
    if total_geral > 0:
        # Percorre cada candidato e seu total de votos.
        for candidato, total in totais.items():
            # Calcula o percentual do candidato em relação
            # ao total geral e arredonda para duas casas decimais.
            percentual = round((total / total_geral) * 100, 2)

            # Armazena o total e o percentual em uma tupla.
            resultado[candidato] = (total, percentual)

    # Retorna o dicionário com o resultado da votação.
    return resultado


# Cria uma lista com os votos de cada sessão eleitoral.
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]


# Chama a função e guarda o resultado da votação.
resultado = resultado_votacao(votos)


# Exibe o resultado na tela.
print(resultado)
