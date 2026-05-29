diamantes = 0
energia = 100

while energia > 0:
    diamantes +=1 #soma + 1
    energia -= 20 #gasta 20 de energia
    print(f"Diamante {diamantes} minerado! Energia restante é: {energia}")
    
    print (f"\nTotal: {diamantes} diamantes minerados!")

