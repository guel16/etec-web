while True: 
    print("\n=== INVENTÁRIO DE LINK ===") #Menu
    print("1. Ver espadas")
    print("2. Ver escudos")
    print("3. Ver poções")
    print("0. Sair")

    opcao = input ("escolha: ") #Pede opção do usuário

    if (opcao == "1") :
        print ("⚔️ Espada do Mestre, Espada Kokiri")
    elif opcao == "2" :
        print ("🛡️ Escudo Hyliano, Escudo Deku")
    elif opcao == "3":
        print ("🧃 Poção Vermelha (HP), Poção Verde (MP)") 
    elif opcao == "0":
        print ("🎒 0Inventário fechado") #Sai do menu
        break
    else:
        print ("Opção invalida! Tente novamente.")