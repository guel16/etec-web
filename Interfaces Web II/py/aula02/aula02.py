nome_piloto =  "Tony Stark"
codinome = "Iron Man"
filiacao = "Vingadores"

# Numeros inteiros (sem casa decimal)
versao_armadura = 85
municao_repulsor = 500

# floats (numero com casa decimal)
nivel_bateria = 98.5
consumo_por_minuto = 2.5

# bool (true or false)
sistemas_online = True
ameaca_detectada = False

# Comando HUD
print ("--- INICIANDO J.A.R.V.I.S ---")
print("Bem-Vindo", nome_piloto)
print("Armadura Ativa: Mark", versao_armadura)

# VERIFICANDO SE O PYTHON GUARDOU OS DADOS
print("\n[DIAGNOSTICO DE MEMORIA]")
print("Variavel 'bateria' é do tipo : ", type (nivel_bateria))
print("Variavel 'online' é do tipo : ", type (sistemas_online))
# VARIAVEIS PARA NOVAS FUNCOES
tempo_voo_restant = nivel_bateria / consumo_por_minuto

print("\n[ESTIMATIVA TÁTICA]")
print("Tempo de voo disponivel: ", tempo_voo_restant, "minutos")

# --- SIMULAÇÃO COMBATE ---
print("\n>>> ALERTA: DISPARANDO UNI-BEAM")
# ATUALIZANDO UM VALOR DE UMA VARIAVEL EXISTENTE 
nivel_bateria = nivel_bateria - 15.5
municao_repulsor = municao_repulsor - 50

print("Status Pós-Combate: ")
print("Bateria", nivel_bateria, "%")
print("Munição", municao_repulsor, "unidades")