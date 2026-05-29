# # Exercicio 1
# x = 1
# while x < 21:
#     print(f"Bloco {x} colocado")
#     x += 1

#  # Exercicio 2
# vidaJogador = 20

# while vidaJogador > 0:
#     vidaJogador -= 3
#     print (f"O zumbi te atacou! Sua vida: {vidaJogador}")

# print ("Você perdeu!")

# # Exercicio 03

# dinheiro = 100
# continuar = "Sim"
# while dinheiro > 0 and continuar == "Sim":
#     comprar = input ("Você quer comprar esmeralda?")
#     if dinheiro < 100:
#         print ("Você acabou de comprar esmeraldas")
#         comprar = input ("Você quer continuar?")
#     else:
#         if dinheiro < 0:
#             print ("Acabou seu dinheiro")
#             comprar = input ("Você quer continuar?")
#         elif (dinheiro < 0):
#             print("Saldo insuficiente")

# Exercicio 4
import random 
vezesTentadas = 0
while vezesTentadas > 0:
    decida = random.choice["pedra" , "ferro" , "ouro" , "diamante"]
    blocos += 4
    vezesTentadas += 1
    if decida == "pedra":
        print (f"{blocos} foi encontrada") 
    elif decida == "ferro" :
        print (f"{blocos} foi encontrado") 
    elif decida == "ouro":
        print (f"{blocos}")
    elif decida == "diamante":
        print (f"{blocos}")
        break
print (f"Tentativas: {vezesTentadas}  blocos encontrado:")

# Exercicio 05
import random
madeiras = 0
pedras = 0
vidros = 0

while madeiras < 20 and vidros < 5 and pedras < 15:
    materiais = random.randint (["madeiras" , "pedras" , "vidros"])

    if materiais == "Madeiras":
        madeiras = random.choice [1,5]
        print (f"Madeiras coletados {madeiras}")
    elif vidros == "vidros":
        vidros = random.choice [1,5]
        print (f"Vidros coloetados {vidros}")
    elif pedras == "pedras":
        pedras = random.choice [1,5]
        print (f"Pedras coletadas {pedras}")
    
print (f"A quantidade de materiais são: {madeiras} , {vidros} , {pedras}")