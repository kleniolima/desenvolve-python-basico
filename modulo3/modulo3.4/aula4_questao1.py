#pedir os dois numeros para o usuario 
num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))

#calculando a soma 
soma = num1 + num2

#verifica se a soma é par ou impar 
if soma % 2 == 0 :
   print ("A soma é par")
else: 
   print ("a soma é impar")