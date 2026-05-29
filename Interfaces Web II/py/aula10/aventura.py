import random

hp = 20
rupees = 100

while True:
    if hp <= 0:
        print("Você morreu... Fim de jogo!")
        break

    print("\n--- MENU ---")
    print("1 - Explorar")
    print("2 - Descansar")
    print("3 - Ver status")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        dano = random.randint(1, 5)
        ganho = random.randint(10, 50)

        hp -= dano
        if hp < 0:
            hp = 0

        rupees += ganho

        print(f"Você explorou, perdeu {dano} de HP e ganhou {ganho} rupees.")

    elif op == "2":
        if rupees >= 20:
            hp += 5
            rupees -= 20
            print("Você descansou e recuperou 5 de HP.")
        else:
            print("Sem rupees suficientes!")

    elif op == "3":
        print(f"HP: {hp}")
        print(f"Rupees: {rupees}")

    elif op == "4":
        print("Saindo do jogo...")
        break

    else:
        print("Opção inválida.")