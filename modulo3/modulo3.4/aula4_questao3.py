#solicita o ano ao usuario
ano = int(input("digite um ano para vermos se ele é bisexto:"))

# verifica se é ou n 
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Nao bissexto")