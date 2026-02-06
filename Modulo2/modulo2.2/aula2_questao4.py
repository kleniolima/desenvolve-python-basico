saldo = 500
juros = 0.01

# 1º mês
saldo = saldo + saldo * juros
print("Mês 1:", saldo)

# 2º mês
saldo = saldo + saldo * juros
print("Mês 2:", saldo)

# 3º mês
saldo = saldo + saldo * juros
print("Mês 3:", saldo)

# Nova mensagem
print("Após 3 meses meu novo saldo é:", saldo)
