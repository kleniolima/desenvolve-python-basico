# Solicita os dados do usuário
genero = input("Digite seu gênero (M/F): ").strip().upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Verifica se a pessoa pode se aposentar
pode_aposentar = (
    (genero == "F" and idade > 60) or      # regra A para mulheres
    (genero == "M" and idade > 65) or      # regra A para homens
    (tempo_servico >= 30) or               # regra B
    (idade >= 60 and tempo_servico >= 25)  # regra C
)

# Imprime True se pode aposentar, False caso contrário
print(pode_aposentar)