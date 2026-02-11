#ler o comprimento como numero inteiro
comprimento = int(input("digite o comprimento do terreno:"))

#ler  a largura do terreno como numero inteiro 
largura = int(input("digite a largura do terreno:"))

#ler o preço do metro quadrado como numero decimal 
preco_m2 = float(input("digite o preço do metro quadrado:"))

#calcular a area do terreno em metros quadrados 
area_m2 = comprimento * largura

# calcula o preço total do terreno 
preco_total = preco_m2 *area_m2

#exibe o resultado com duas casas decimais 
print(f"o terrreno possui {area_m2}m2 e custa R${preco_total:,.2f}")