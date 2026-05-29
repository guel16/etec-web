notaFinal = int(input("Digite a nota final: "))
if notaFinal >= 7:
    print("APROVADO")
elif notaFinal >= 5 and notaFinal < 7:
    print("RECUPERAÇÃO!")
else:
    print ("REPROVADO!")
