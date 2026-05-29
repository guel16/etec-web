ruppes = 300

while True:
    print (f"\n=== LOJA DA VILA KAKARIO === (Ruppes: {ruppes})")
    print("1. Poção Vermelha - 50 rupees")
    print("2. Arco e Flechas - 150 rupees")
    print("3. Bomba - 30 rupees")
    print("0. Sair da loja")

    opcao = input("Escolha: ") #Pede opção

    if opcao == "1":
        if ruppes >= 59:
            ruppes -= 50
            print ("Poção Vermelha comprada!")
        else:
            print ("Ruppes insuficientes!")
    elif opcao == "2":
        if ruppes >= 150:
           ruppes -= 150
    elif opcao == "3":
        if ruppes >= 30:
           ruppes -= 30
           print ("Bomba comprada")
    elif opcao == "0":
        print (f"Saindo da loja. Ruppes restantes: {ruppes}")
        break
    else:
        print ("Digite um valor valido! ")

# isalpha() => apenas letra, não conta numero
# strip() => remove espaco
# try/except => tratamento de erro
