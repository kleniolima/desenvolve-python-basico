# Função que verifica se um triângulo é equilátero
def testa_equilatero(lados):
    # Um triângulo é equilátero quando os três lados são iguais
    return lados[0] == lados[1] == lados[2]


# Lista contendo os lados de vários triângulos
triangulos = [
    [2, 2, 2],
    [3, 4, 5],
    [3, 2, 2],
    [4, 4, 4]
]

# filter() aplica a função testa_equilatero a cada triângulo
# list() transforma o resultado em uma lista
equilateros = list(filter(testa_equilatero, triangulos))

# Exibe somente os triângulos equiláteros
print(equilateros)
