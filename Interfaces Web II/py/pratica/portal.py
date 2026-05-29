# Captalize deixa as letras em maiusculas
# Strip Lower apaga espaco
temLanterna = input("Tens lanterna? ").capitalize()
temCoragem = input("Tens coragem? ").capitalize()
if temLanterna == "True" and temCoragem == "True":
    print ("Acesso Permitido")
else :
    print("Aceso negado")