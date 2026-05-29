# nivelCansaco = int(input("Qual é o nivel de cansaco (0-100)"))
# fome = input("Voce esta com fome? True/False?")
# if nivelCansaco > 80 or fome == 'True':
#     print("Poderes desativados")

#     # 
#     canal = int(input("Qual é o seu canal? (1 ou 2)"))

#     match canal:
#         case 1:
#             print("Sincronização Russia"),
#         case 2:
#             print("Sincronização Shopping")
#         case _:
#             print("Apenas ruido")

#             # 
# temArma = input("Voce tem arma?")
# temMunicao= input("Tem munição?")
# pertoSaida = input("Está perto da saida?")

# if (temArma and temMunicao) or pertoSaida:
#     print("Hopper Sobreviveu")
# else:
#     print("Hopper Morreu")

#     # 

nomeMusica = input("Nome da musica favorita:")
walkmanLigado = input ("Está ligado (True/False)")
maxTranse = input("Max está em transe (True/False)")

if maxTranse == 'True' and walkmanLigado == 'True' and nomeMusica == "Running Up That Hill":
    print("Ela escapou do Vecna!")

elif maxTranse == 'True' and walkmanLigado == 'False':
    print("Corra Lucas!")
else:
    print("Tudo calmo em Hawkins por enquanto...")