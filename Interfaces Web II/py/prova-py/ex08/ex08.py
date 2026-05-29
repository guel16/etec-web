idadePessoa = int(input("Qual é a idade: "))
temDocumento = bool(input("Possui documento? (TRUE OR FALSE)"))
estaAcompanhado = input("Está acompanhado? (TRUE OR FALSE)")

if (idadePessoa >= 18)  and (temDocumento == 'True') or (estaAcompanhado == 'True'):
    print("PODE ENTRAR")
else:
    print("NÃO AUTORIZADO!")