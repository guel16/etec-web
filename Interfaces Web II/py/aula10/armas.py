while True :
    print (f"Espada")
    print (f"Arco")
    print (f"Bomba")
    print (f"Sair")
    
    try:
        decidaEquipamento = int (input("Escolha seu equipamento "))
    except ValueError:
        print("Digite um equipamento valido!") 
    match decidaEquipamento:
        case 1:
            print ("Você pegou a espada");
        case 2:
            print ("Você pegou o arco")
        case 3:
            print ("Você pegou bomba")
        case 4:
            break
        case _:
            print ("Escolha um equipamento valido!")
        