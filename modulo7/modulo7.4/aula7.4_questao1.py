# importa a biblioteca pathlib 
# ela ajuda a trabalhar com pastas e arquivos 
from pathlib import Path


# descobre a pasta onde este arquivo python esta salvo
# __file__ representa o proprio script q esta sendo executado
pasta_do_script = Path(__file__).resolve().parent


# cria o caminho completo do arquivo frase.txt
# o arquivo ficará na mesma pasta do script
caminho_do_arquivo = pasta_do_script / "frase.txt"


# pede para o usuario digitar uma frase 
# a frase fica guardada dentro da variavel frase
frase = input("digite uma frase:")


# Abre o arquivo para escrever 
# "w" significa escrever
# encoding="utf-8" permite salvar acentos corretamente
with open(caminho_do_arquivo, "w", encoding="utf-8") as arquivo:

    # Escreve a frase dentro do arquivo
    arquivo.write(frase)



# mostra uma msg informando que o arquivo foi salvo
print(f"Frase salva em {caminho_do_arquivo}")