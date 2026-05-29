log_bruto = " ID_2026-SECTOR_A4-TEMP_75C "
# Strip remove espaco do comeco e do final
log_limpo = log_bruto.strip()

 #Estrair do caractere 3 a 7
id_sistema = log_limpo[3:7] 
print(id_sistema)

setor = log_limpo[8:16]
print(setor)

# Transformacao em maiusculo
print("Log em maiusculas: ", log_limpo.upper())
# Minusculas
print("Logem minusculas:", log_limpo.lower())
# Formatação (substituir)
log_formatado = log_limpo.replace ("-", "")
print("Log Formatado: ", log_formatado)

# divisao de dados (Split)
componentes = log_limpo.split ("-")
print("\nLista de Componentes: ", componentes)

tem_setor_a  =  "SECTOR_A" in log_limpo
print (f"O log pertence ao Setor A? {tem_setor_a}" )

codigo_secreto = "TX-990"
codigo_invertido = codigo_secreto[::-10]
print(f"O codigo reverso: {codigo_invertido}")