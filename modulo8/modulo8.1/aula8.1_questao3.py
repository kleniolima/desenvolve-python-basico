# lista contendo os conjuntos de interesses de cada turma
turmas = [
    {'ações comunitarias', 'futebol', 'música', 'rugby'},
    {'ações comunitarias', 'musica', 'rugby', 'teatro'},
    {'musica', "rugby", 'teatro', 'vôlei'},
    {'musica', "vôlei", "rugby"},
     {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'futebol', 'rugby'},
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'rugby', 'vôlei'}
]

# encontra as atividades que aparecem em tdas as turmas
atividades_comuns = set.intersection(*turmas)

# mostra o conjunto de atividades comuns
print(atividades_comuns)