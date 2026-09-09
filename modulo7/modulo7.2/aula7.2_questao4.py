# criar uma função chamada validador_senha
# ele recebe uma senha como informação
def validador_senha(senha):

    # verifica se a senha tem pelo meno 8 caracteres
    
    tem_tamanho_minimo = len(senha) >= 8

    # verifiva se existe pelo menos uma letra maiuscula
    tem_letra_maiuscula = any(
        caractere.isupper()
        for caractere in senha
    )

    # verifica se existe pelo menos uma letra minuscula
    tem_letra_minuscula = any(
        caractere.islower()
        for caractere in senha
    )

    # verifica se existe pelo menos um caractere especial
    # um caractere especial é aql q nao é letra nem numero ( &,%,$,@)

    tem_caractere_especial = any(
        not caractere.isalnum()
        for caractere in senha
    )

    # verifica se existe pelo menos um numero
    tem_numero = any(
        caractere.isdigit()
        for caractere in senha
    )

    # a senha só será valida se tudo for verdade verdadeira
    if (
        tem_tamanho_minimo
        and tem_letra_maiuscula
        and tem_letra_minuscula
        and tem_numero
        and tem_caractere_especial
    ):

        # retorna True quando a senha é valida 
        return True

    else: 

        # retorna False qd a senha não é valida 
        return False

    # Chama a função e testa uma senha válida
print(validador_senha("Senha123@"))

# Chama a função e testa uma senha sem maiúscula,
# sem número e sem caractere especial
print(validador_senha("senhafraca"))

# Chama a função e testa uma senha sem número
print(validador_senha("Senha_fraca"))