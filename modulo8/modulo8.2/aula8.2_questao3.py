# Define uma função que recebe uma lista de tuplas
def ordenar_tuplas(alunos):
    # Cria e retorna uma nova lista ordenada
    # A ordenação será feita pela média de cada aluno
    # A média está na posição 1 de cada tupla
    # reverse=True organiza da maior média para a menor
    return sorted(alunos, key=lambda aluno: aluno[1], reverse=True)


# Cria uma lista contendo tuplas com nome e média dos alunos
alunos_notas = [
    ('Alice', 8.5),
    ('Bob', 7.2),
    ('Charlie', 9.0),
    ('David', 8.8)
]

# Chama a função e guarda a lista ordenada
resultado = ordenar_tuplas(alunos_notas)

# Mostra a lista ordenada
print(resultado)
