#avaliação em escala de 1 a 5
num = int(input("De uma nota para o filme de 1 a 5: "))
if num == 5:
    print("Excelente")
elif num == 4 :
    print("Muito bom")
elif num == 3:
    print("Bom!")
elif num == 2: 
    print("Regular")
elif num == 1:
    print("Ruim")
else:
    print("Avaliação invalida, digite um numero de 1 a 5: ")