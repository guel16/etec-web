ruppes = 500
while ruppes > 0:
    print("\nSaldo:", ruppes)
    print("1 - Poção de Velocidade (100)")
    print("2 - Poção de Agilidade (150)")
    print("3 - Poção de Tranquilidade (200)")
    
    try:
        escolhaItem = int(input("Escolha a poção para comprar: "))
    except ValueError:
        print("Digite um valor válido")
        continue

    if escolhaItem == 1:
        if ruppes >= 100:
            ruppes -= 100
            print("Parabéns, você comprou Poção de Velocidade")
        else:
            print("Saldo insuficiente")
    elif escolhaItem == 2:
        if ruppes >= 150:
            ruppes -= 150
            print("Parabéns, você comprou Poção de Agilidade")
        else:
            print("Saldo insuficiente")
    elif escolhaItem == 3:
        if ruppes >= 200:
            ruppes -= 200
            print("Parabéns, você comprou Poção de Tranquilidade")
        else:
            print("Saldo insuficiente")
    else:
        print("Escolha uma opção válida")

print(f"\nSeu saldo final: {ruppes}")