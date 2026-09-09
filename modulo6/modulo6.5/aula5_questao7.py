def avalia_tabuleiro (tabuleiro):
   # verifica as linhas horizontais 
   for linha in tabuleiro:
       if linha[0] != ' ' and linha[0] == linha [1] == linha [2]:
          return linha [0]



   # verifica as colunas verticais 
   for coluna in range(3):
       if (tabuleiro[0][coluna] != ' 'and
           tabuleiro[0][coluna] == tabuleiro[1][coluna] and 
           tabuleiro[0][coluna] == tabuleiro[2][coluna]):

           return tabuleiro[0][coluna]

   # verifica a diagonal que começa no canto superior esquerdo 
   if (tabuleiro[0][0]  != ' 'and
       tabuleiro[0][0]  == tabuleiro[1][1] and 
       tabuleiro[1][1]  == tabuleiro[2][2]):

       return tabuleiro[0][0]


   # Verifica a diagonal que começa no canto superior direito
   if (tabuleiro[0][2] != ' ' and
        tabuleiro[0][2] == tabuleiro[1][1] and
        tabuleiro[1][1] == tabuleiro[2][0]):

        return tabuleiro[0][2]

   # Se nao encontrou vencedor dar empate
   return "Empate" 

tabuleiro = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'O']
]
resultado = avalia_tabuleiro(tabuleiro)

print(resultado)
    