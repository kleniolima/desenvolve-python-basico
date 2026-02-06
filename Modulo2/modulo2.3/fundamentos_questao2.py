# Dados do trabalhador
salario_hora = 20
horas_semana = 40

# 1️⃣ Salário semanal bruto
salario_bruto = salario_hora * horas_semana
print("Salário semanal bruto: R$", salario_bruto)

# 2️⃣ Salário líquido com todos os descontos (INSS 10% + Sindicato 5%) em uma só expressão
salario_liquido = salario_bruto - (salario_bruto * 0.10 + salario_bruto * 0.05)
print("Salário semanal líquido: R$", salario_liquido)
