print ("--- SISTEMAS DE RH v1.0 ---")
# entrada de dados (texto)
nome = input ("Digite o nome completo: ")

# Entrada de dados (numeros)
idade = int(input("Digite a idade: "))
salario_atual = float(input("Digite o salario atual: "))

# Processamento de dados
ano_aposentadoria = 2026 + (65 - idade)
novo_salario = salario_atual * 1.10 #Aumento de 10%

# Saida formatada (F-STRINGS)
print("\n---FICHA REGISTRADA---")
print(f"Funcionario {nome}")
print(f"Idade registrada: {idade} anos")
print(f"Ano estimado de reforma: {ano_aposentadoria}")
print(f"Salario projetado: R$ {novo_salario:2f}")