cargo = input("Cargo (Admin/User/Guest): ").capitalize()
tentativas = int(input("Tentativas de login hoje: "))
sistema_ativo = True

# USO DE OPERADORES LOGICOS

if cargo == "Admin" and tentativas < 5 :
    print ("\n[ACESSO TOTAL CONCEDIDO]")
elif cargo == "User" or cargo == "Admin":
    print("\n[ACESSO RESTRITO CONCEDIDO]")

else:
    print("\n[ACESSO NEGADO]")

# USO DE MATCH CASE (para selecoes diretas)
print("\n--- CONFIGURAÇÕES DE PERFIL ---")
match cargo:
    case "Admin":
        print("Painel: Editar, Apagar e Criar")
    case "User":
        print("\nPainel: Vizualizar, Editar Proprio")
    case "Guest":
        print("Painel: Apenas Leitura")
    case _: # Caso padrão (default)
        print("Cargo não identificado no sistema.")
