#solicitar a idade do lek
idade = int(input("Digite a sua idade : "))

#pergunta se ja jogou pelo menos 3 jogos de tabuleiro
jogou_3_ou_mais = input("voce ja jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
jogou_3_ou_mais = jogou_3_ou_mais.strip().lower() == "true"

#perguta quantas vezes ja venceu 
vitorias = int(input("Quantas vezes vc ja venceu um jogo ?"))

#verifica se o meno pode entrar no squad
pode_entrar = (16 <= idade <= 18) and jogou_3_ou_mais and(vitorias >= 1)

#imprime True se puder entrar, false se nop 
print(pode_entrar)