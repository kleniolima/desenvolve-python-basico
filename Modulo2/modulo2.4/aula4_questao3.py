#pergunta o nome do produto 1 
nome1 = input("Digite o nome do produuto 1:")

#perguntar o preço unitario do produto 1 
preco1 = float(input("digite o preço unitário do produto 1 :"))

#perguntar a quantidade do prodito 1 
quantidade1 = int(input("digite a quantidade do produto 1 :"))

#pergutar o nome do produto 2 
nome2 = input("Digite o nome do produto 2 :")

#perguntar o preço unitário do produto  2 
preco2 = float(input("digite o preço unitário do produto 2 :"))

# perguntar a quantidade do produto 2 
quantidade2 = int(input("digite a quantidade do produto 2 :"))

#perguntar o nome do produto 3 
nome3 = input("Digite o nome do produto 3:")

#perguntar o preço unitario do produto 3 
preco3 = float(input("Digite o preço unitário do produto 3 :"))

#perguntar a quantidade do produto 3
quantidade3 = int(input("Digite a quantidade do produto 3:")) 

#calcular o preço total do produto 1 
total1 = preco1 * quantidade1

#calculando preço total do produto 2 
total2 = preco2 * quantidade2

#calculando preço total do produto 3 
total3 = preco3 * quantidade3

#calcula prço total da compra 
preco_total = total1 + total2 + total3

print(f"Total: R${preco_total:,.2f}")