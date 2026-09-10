# pergunta qts pessoas estao na fila
quantidade_de_pessoas = int(input("Quantas pessoas estao na fila ?"))

# cria uma lista vazia para guardar as tuplas
# cada tupla terá o nome e a idade de uma pessoa
pessoas = []

# repete o cadastro conforme a quantidade informada
for contador in range(quantidade_de_pessoas):

    # mstra qual pessoa esta sendo cadastrada
    print(f"\nCadastro da pessoa {contador + 1}")

    # pede o nome da pessoa 
    nome = input("Digite o nome: ")

    # pede a idade da pessoa e converte oo texto para numero inteiro
    idade = int(input("Digite a idade "))

    # cria uma tupla com o nome e a idade 
    pessoa = (nome, idade)

    # adciona a tupla à listas de pessoas
    pessoas.append(pessoa)

# cria uma lista vazia para guardar os nomes dos menores de idade
menores_de_idade = []

# Cria uma lista vazia para guardar os nomes dos maiores de idade
# Esta linha precisa existir antes do próximo for
maiores_de_idade = []


# percorre cada tupla armazenada na lista de pessoas
for nome, idade in pessoas:

    # verifica se a pessoa tem menos de 18 anos
    if idade < 18:

        # adciona o nome na lista dos menozin
        menores_de_idade.append(nome)

    else:
        # se a idade for 18 ou mais adc a maiores de idade
        maiores_de_idade.append(nome)

# Converte a lista de menores em uma tupla
tupla_menores = tuple(menores_de_idade)

# Converte a lista de maiores em uma tupla
tupla_maiores = tuple(maiores_de_idade)


# Imprime a tupla com os nomes dos menores de idade
print("\nMenores de idade, que não podem entrar:")
print(tupla_menores)

# Imprime a tupla com os nomes dos maiores de idade
print("\nMaiores de idade, que podem entrar:")
print(tupla_maiores)