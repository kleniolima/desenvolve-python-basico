# Cria uma função que ordena strings pelo tamanho
def ordena_por_comprimento(lista):
    # sorted() ordena a lista
    # key=lambda texto: len(texto) usa o comprimento de cada string
    resultado = sorted(lista, key=lambda texto: len(texto))

    # Retorna a lista ordenada
    return resultado


# Lista de nomes
nomes = [
    "Joao",
    "Maria",
    "Jose",
    "Gabriela",
    "Sol",
    "Luna",
    "Bento",
    "Enzo",
    "Fernanda"
]

# Aplica a função à lista de nomes
nomes_ordenados = ordena_por_comprimento(nomes)

# Imprime o resultado
print(nomes_ordenados)
