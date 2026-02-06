
# Dados do trabalhador
salario_hora = 20       # valor por hora
horas_semana = 40       # horas trabalhadas na semana

# Cálculo do salário bruto
salario_bruto = salario_hora * horas_semana

# Cálculo dos descontos
desconto_inss = salario_bruto * 0.10      # 10% do bruto
desconto_sindicato = salario_bruto * 0.05 # 5% do bruto

# Cálculo do salário líquido
salario_liquido = salario_bruto - (desconto_inss + desconto_sindicato)

# Impressão dos resultados
print("Salário semanal bruto: R$", salario_bruto)
print("Desconto INSS (10%): R$", desconto_inss)
print("Desconto sindicato (5%): R$", desconto_sindicato)
print("Salário semanal líquido: R$", salario_liquido)