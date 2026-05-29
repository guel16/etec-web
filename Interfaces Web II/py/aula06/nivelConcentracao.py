nivelConcentracao = int(input("Qual é o nivel de concentracao (0-100)"))

if nivelConcentracao > 80 :
    print("Espelliarmus Perfeito!")
    if nivelConcentracao  >=50 and nivelConcentracao < 80 :
        print("Feitico fraco, tente novamente");
elif nivelConcentracao < 50:
    print("A varinha falhou");
