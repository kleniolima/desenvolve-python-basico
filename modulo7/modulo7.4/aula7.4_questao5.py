# abre o arquivo "(meus_livros.csv)" para escrita
#o "w" significa write, q quer dizer escrever
# o enconding="utf-8" permite usar acentos corretamente
arquivo = open("meus_livros.csv", "w", encoding="utf-8")

# escreve a primeira linha do arquivo
# essa linha contem os nomes das colunas
# o \n faz o cursor pular para a proxima linha
arquivo.write("Título,Autor,Ano de publicação,Número de paginas\n")

# escreve as informaçoes do primeiro livro
arquivo.write("A arte da Guerra,Sun Tzu, século V a.C.,104\n")

# escreve as informaçoes do segundo livro 
arquivo.write("Os Segredos do Lobo,Jordan Belfort,2018,288\n")

# escreve as informaçoes do terceiro livro
arquivo.write("Mais Esperto que o Diabo,Napoleon Hill,1938,200\n")

#escreve as informaçoes do quarto livro 
arquivo.write("Os Axiomas de Zurique,Max Gunther,1985,176\n")

# escreve as informaçoes do quinto livro
arquivo.write("Cartas de um Diabo a Seu Aprendiz,C.S.Lewis,1942,208\n")

# escreve as informaçoes do sexto livro
arquivo.write("Pai Rico Pai Pobre,Robert Kiyosaki,1997,366\n")

#escreve as informaçoes do setimo livro
arquivo.write("Manual de Persuasão do FBI,Jack Schafer,2015,256\n")

#escreve as informacoes do oitavo livr
arquivo.write("O Corpo Fala,Pierre Weil,1980,288\n")

#escreve as informacoes do nono livro
arquivo.write("Salomao o Homem Mais Rico que já Existiu,Stven K. Scott,2020,163\n")

#escreve as informações do decimo livro
arquivo.write("O Principe,Nicolau Maquiavel,1532,176\n")

#fecha o arquivo
# isso salva tudo q foi escrito
arquivo.close()

# Mostra uma msg no terminal informando q cabou
print("O arquivo meus_livros.csv foi criado com sucesso !")