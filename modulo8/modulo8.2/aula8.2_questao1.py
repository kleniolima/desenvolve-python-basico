# define uma função que recebe uma tupla com as dimensoes 
def calcula_area_perimetro(dimensoes):
    # retira o primeiro valor da tupla e guarda como largura
    largura = dimensoes[0]


    # retira o segundo valor da tupla e guarda como comprimento 
    comprimento = dimensoes[1]

    # calcula a area do terreno 
    area = largura * comprimento

    # calcula o perimetro do terreno 
    perimetro = 2 * (largura + comprimento)

    # retorna a area e o perimetro
    return area, perimetro

# Pede a largura do terreno ao usuário
largura = float(input("Digite a largura do terreno: "))

# Pede o comprimento do terreno ao usuário
comprimento = float(input("Digite o comprimento do terreno: "))

# cria uma tupla com a largura e o comprimento do terreno 
dimensoes = (largura, comprimento)

# chama a função e guarda os dois resultados 
area, perimetro = calcula_area_perimetro(dimensoes)

# mostra a area calculada 
print(f"Area: {area}")

# Mostra o perímetro calculado
print(f"Perímetro: {perimetro}")