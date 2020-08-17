import random
caracteres = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '*','_','@','Ç','#','&','$',
    '0','1','2','3','4','5','6','7','8','9'
]

def gerar_senha(caracteres,tamanho_senha):
    senha = ''
    while len(senha) < tamanho_senha:
        senha += random.choice(caracteres)
    return senha

