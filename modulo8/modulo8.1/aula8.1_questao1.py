# guardar a frase em uma variavel
frase = "O rato roeu a roupa do Robson"

# transforma a frase em um SET para remover carcteres duplicados
# Maiusculas e minusculas continuam sendo diferentes
caracteres_unicos = set(frase)

# ordena os caracteres unicos em ordem alfabetica
caracteres_ordenados = sorted(caracteres_unicos)

# mostra os caracteres unicos e ordenados
print(caracteres_ordenados)