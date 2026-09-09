# Importa a biblioteca math para usar o valor de pi
import math

# Lista contendo os raios das circunferências
raios = [1.5, 0.8, 2.3, 5.0]

# map() aplica a função lambda a cada raio da lista
# A função lambda calcula:
# pi * (raio ** 2)
# round(..., 2) arredonda o resultado para 2 casas decimais
areas = list(
    map(
        lambda raio: round(math.pi * (raio ** 2), 2),
        raios
    )
)

# Exibe a lista com as áreas calculadas
print(areas)
