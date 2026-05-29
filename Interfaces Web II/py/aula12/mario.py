personagens = ["Mario" , "Luigi", "Peach" , "Toad" , "Yoshi"]

for personagens in personagens:
    print (f"{personagens} entrou em fase!")

itens =["Cogumelos" , "Estrela" , "Flor de Fogo" , "Pena"]

for indice, item in enumerate(itens):
    print (f"Slot {indice}: {itens}")

nome = "MARIO"

for indice, letra in enumerate(nome):
    print (f"Slot: {indice}: {letra}")

frase = "Super Mario Bros"
vogais = "aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1
        print (f"Total de vogais: {contador}")

mundos = ["Mundo 1" , "Mundo 2" , "Mundo 3"]
fase = ["Fase 1" , "Fase 2" , "Fase 3" , "Fase 4"]

for mundos in mundos:
    print (f"\n=== {mundos} ===")
    for fase in fase:
        print (f"{mundos} - {fase}")

jogadores = [
    {"Nome": "Mario", "moedas": 150},
    {"Nome": "Luigi", "moedas": 120},
    {"Nome": "Peach", "moedas": 200},
    {"Nome": "Toad", "moedas": 80}
]

print ("=== RANKING MOEDAS ===")
for posicao, jogador in enumerate(jogadores, start=1):
    print (f"{posicao}º lugar: {jogador['moedas']} moedas")

