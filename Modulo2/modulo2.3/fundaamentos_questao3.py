# Valor em reais
valor_brl = 100  # você pode alterar para qualquer quantia

# Taxa de câmbio: 0.69 BRL = 1 CNY
taxa_cambio = 0.69

# Cálculo do valor equivalente em yuan
valor_cny = valor_brl / taxa_cambio

# Impressão do resultado
print("R$", valor_brl, "equivalem a CNY", round(valor_cny, 2))
