#impota a biblioteca random, usada para gerar numeros aleatórios 
import random

# importa a biblioteca math, usada para calcular a raiz quadrada 
import math

# pergunta ao usuario quantos numeros devem ser sorteados 
# int () transforma a resposta em um numero inteiro 
quantidade = int(input("quantos numeros vc quer sortear ?"))

# cria uma variavel para guardar a soma dos numeros 
# ela começa com zero pq ainda nao sorteamos nenhum valor 
soma = 0

# repete o codigo abaixo a quantidade de vezes escolhida pelo user 
for contador in range (quantidade):
# sorteia um numero inteiro entre 0 e 100 
    numero = random.randint (0,100)
# mostra na tela o numero que foi sorteado 
    print ("Numero sorteado:", numero)
# adciona o numero sorteado à soma 
    soma = soma + numero

#calcula a raiz quadraa da soma dos numeros 
    raiz = math.sqrt(soma)
# mostra a soma final 
    print ("Soma dos valores:", soma)
#mostra a raiz quadrada da soma com duas casas decimais 
    print(f"raiz quadrada da soma:  {raiz:.2f}")