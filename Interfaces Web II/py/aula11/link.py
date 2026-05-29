while True :
    entrada = input ("Quantos rupees quer gastar? ")

    # Verifica se o numero positivo
    if entrada.isdigit() and int(entrada) > 0:
        rupees = int(entrada)
        print(f"Voce gastou {rupees} ruppes") 
        break
    print ("Valor invalido! Digite um numero positivo")


