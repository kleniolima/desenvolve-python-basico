# Solicitar os dados 
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

#pega a distancia 
if distancia <= 100:
    valordo_frete = peso * 1
elif distancia <= 300:
    valordo_frete = peso * 1.5
else: 
    valordo_frete = peso * 2 

#taxa do amor 
if peso > 10:
   valordo_frete += 10 

print(f"valor do frete : R${valordo_frete:.2f}")