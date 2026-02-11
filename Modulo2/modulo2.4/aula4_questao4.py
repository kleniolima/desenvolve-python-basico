# lê a quantia em reais 
valor = int(input("Digite o valor em reais :"))

#criar lista de notas 
notas = [100, 50, 20, 10, 5, 2, 1]
for nota in notas:
    qtd = valor // nota 
    print(f"{qtd} nota(s) de R${nota},00")
    valor = valor % nota