while True:
    try:
        vida = int(input("Vida de Ling (1-20)"))
        if 1<= vida <= 20:
            print (f"Vida definida: {'❤️' * vida}")
            break
        else:
            print ("Escolha entre 1 e 20")
    except ValueError:
        print ("Digite um numero valido: ")
