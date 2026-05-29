tempoProva = int(input("Tempo da prova (em segundos)"))
criaturasDerrrotadas = int(input("Criaturas derrotadas"))

if tempoProva < 300 and criaturasDerrrotadas > 5:
    print("Trofeu Ouro")
elif tempoProva < 300 or criaturasDerrrotadas > 5 :
    print("Trofeu Prata")
else:
    print("Certificado de Participação")