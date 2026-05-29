# O PROGRAMA INICIA SORTEANDO UM NUMERO ALEATORIO ENTRE 0-100
# INPUT COM (OLA USUARIO VAMOS BRINCAR DE ADIVINHAR)
# EU PENSEI EM UM NUMERO ENTRE 0-100
# QUAL VC ACHA Q É
# WHILE (SE ELE ACERTOU É PRA EXIBIR: PARABENS VOCE É INCRIVEL) 
# SE NAO ACERTOU (ESTE NUMERO É < DO QUE VC FALOU

import random

numeroSorte = random.randint (1, 100)
escolha = 0

print ("Ola usuario vamos brincar de adivinhar?");
print ("Eu pensei em um numero de 0-100");
numeroUsuario = input ("Qual você acha que é? ");

while escolha != numeroSorte :
    if (numeroSorte == numeroUsuario):
        print ("Parabens, você é um genio!")
    else:
        if (escolha < numeroSorte):
            print ("Você errou")
            print ("O numero é menor do que você falou!")
            numeroUsuario = input ("Digite novamente ");
        elif (escolha > numeroSorte) :
            print ("Você errou!")
            print ("O numero é maior")
            numeroUsuario = input ("Digite novamente ");
