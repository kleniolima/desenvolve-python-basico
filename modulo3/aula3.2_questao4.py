#Solicita a classe do personagem
classe = input("Escolha a classe do personagem (guerreiro, mago, arqueiro): ").strip().lower()

#Solicita os pontos de atributos 
forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

# Verifica se os atributos são consistentes com a classe
if classe == "guerreiro":
    ficha_valida = forca >= 15 and magia <= 10
elif classe == "mago":
    ficha_valida = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    ficha_valida = (5 < forca <= 15) and (5 < magia <=15)
else:
    ficha_valida = False #classe invalida 

# Imprime True  se os atributos sao consistentes, False ao contrário k
print(ficha_valida)
