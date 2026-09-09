def pares_unicos(numeros, soma_objetivo):
    # Conjunto para armazenar os pares sem duplicatas
    pares = set()

    # Percorre todos os elementos da lista
    for i in range(len(numeros)):
        # Começa no elemento seguinte para não repetir combinações
        for j in range(i + 1, len(numeros)):
            primeiro = numeros[i]
            segundo = numeros[j]

            # Verifica se a soma dos dois elementos é igual ao objetivo
            if primeiro + segundo == soma_objetivo:
                # Ordena os valores dentro do par
                par = tuple(sorted((primeiro, segundo)))

                # Adiciona o par ao conjunto
                pares.add(par)

    # Retorna os pares ordenados
    return sorted(pares)


# Exemplo de uso
nums = [3, 4, 5, 6, 7]
soma = 10

resultado = pares_unicos(nums, soma)

print(resultado)
