nomePersonagem = input("Qual é o nome do personagem? (Eleven/Dustin/Steve) ").capitalize()

match nomePersonagem :
    case "Eleven":
        print("Poderes Psiquicos")
    case "Dustin":
        print("Especialista em Radio")
    case "Steve":
        print ("O Babá")
    case _:
        print("Personagem invalido")