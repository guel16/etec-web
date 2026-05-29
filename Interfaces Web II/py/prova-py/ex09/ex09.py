cadastrar = int(input("CADASTRAR ALUNO"))
exibir = input("EXIBIR NOTAS")
sair = input("SAIR")

match cadastrar:
    case 1:
        print("Pode cadastrar aluno.")
    case 2:
        print("Pode exibir.")
    case 3 :
          print("Fechando sistema...")