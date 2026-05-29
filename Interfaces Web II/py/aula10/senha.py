senha_correta = "TRIFORCE"
tentativas = 0
maximo_tentativas = 3

while tentativas < maximo_tentativas:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso concedido!")
        break
    else:
        tentativas += 1
        print("Senha incorreta.")
        
if tentativas == maximo_tentativas:
    print("Bloqueado!")