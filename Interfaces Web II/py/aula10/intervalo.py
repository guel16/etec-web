while True:
    entrada = input ("Escolha o nivel de dificuldade (1 a 3): ")

    if entrada.isdigit():
        nivel = int(entrada)
        if 1<= nivel <= 3:
            print (f"Dificuldade {nivel} selecionada!")
        break
    print ("Inválido! Escolha 1, 2 ou 3")

    # isdigit() => verifica se é numero
    