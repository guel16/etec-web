import random 

vida = 100 
passos = 0

while vida > 0:
    passos += 1
    encontro = random.choice (["Nada", "Nada", "Diamante", "Creeper"]);

    if encontro == "Crepper":
        print (f"Passo {passos}: CREEPER! Fugindo");
        break
    elif encontro == "Diamante":
        print (f"Passo {passos}: Diamante encontrado!");
    else:
        print (f"Passo {passos}: Nada por aqui...");
    
print(f"Exploração encerrada após {passos} passos");

itens = ["Madeira" , "Pedra" , "Lixo" , "Ferro" , "Lixo" , "Diamante"]
indice = 0

while indice < len(itens):
    item = itens[indice]
    indice += 1

    if item == "Lixo":
        continue #Pula itens de lixo
    
    print (f"Item coletado: {item}")
    