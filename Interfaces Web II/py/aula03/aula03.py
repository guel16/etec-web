# Entrada de dados
produtos = "Notebook Gamer"
preco_uinitario = 4500.00
quantidade = 3

# Calculo

total_bruto = preco_uinitario * quantidade

# Calculo de desconto
preco_desconto = total_bruto
fator_desconto = 0.15
valor_desconto = total_bruto * fator_desconto
total_liquido = total_bruto - preco_desconto
print(total_liquido)

# NOTA FISCAL

print("--- NOTA FISCAL ---")
print("Produto:", produtos)
print("Total bruto: R$", total_bruto)
print("Desconto aplicado: R$", valor_desconto)
print("Total a pagar: R$", total_liquido)

# PARCELAMENTO  (Divisão)
parcelas = 12
valor_parcela = total_bruto / parcelas
print("\n--- OPERAÇÃO PARCELADA ---")
print("12x de R$", valor_parcela)

# 5. PRECEDENCIA MATEMATICA
# Calculo de media de vendas da semana
vendas_seg = 1200
vendas_ter = 3400
vendas_qua = 5000
media_vendas = (vendas_seg + vendas_ter + vendas_qua) / 3
print("\nMédia de vendas (3 dias): R$", media_vendas)

# // deixa em inteiro, / deixa inteiro