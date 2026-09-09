# Lista com os nomes dos meses.
# A posição 0 fica vazia porque janeiro será o índice 1.
meses = [
    "",
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]


# Solicita a data de nascimento ao usuário
data = input("Digite uma data de nascimento: ")

# Divide a data usando a barra como separador
# Por exemplo: "29/10/1973" vira ["29", "10", "1973"]
dia, mes, ano = data.split("/")


# Converte o mês de texto para número inteiro
numero_mes = int(mes)

# Busca o nome do mês na lista
nome_mes = meses[numero_mes]


# Exibe a data formatada
print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")
