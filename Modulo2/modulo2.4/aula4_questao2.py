#ler a temperatura como numero inteiro
temperatura = int(input("digite a temperatura Fahrenheit que será convertida : "))

#converter para celcius
celsius = int((temperatura-32) * 5/9)

#exibe o resultado com duas casas decimais 
print(f"{temperatura} graus Fahrenheit são {celsius} graus Celsius")
