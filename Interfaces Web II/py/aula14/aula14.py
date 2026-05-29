def ficha_ninja (nome, vila, rank="Genin"):
    print(f"Ninja: {nome}")
    print(f"Vila: {vila}")
    print(f"Rank: {rank}")
    print("---")

ficha_ninja("Naruto" , "Vila da Folha")
ficha_ninja("Kakashi" , "Vila da Folha" , "Jonin")


def jutsu(nome, tipo, dano):
    print(f"{nome} ({tipo}) - Dano {dano}")

jutsu("Rasengan" , "Vento" , 500)

jutsu(dano=800, nome="Chidori", tipo="Raio")

def analisar_combo(ataque):
    total = sum(ataque)
    media = total / len(ataque)
    maior = max(ataque)
    return total , media , maior

combo = [200 , 350 , 150 , 400]
total , media , maior = analisar_combo(combo)

print(f"Dano total: {total}")
print (f"Dano médio: {media}")
print (f"Dano maior: {maior}")

def invocar_clones(*nomes):
    print (f"Kage Bunshin no Jutsu! {len(nomes)} clones invocados!")
    for i, nome in enumerate(nomes , start=1):
        print(f"Clone: {i}: {nome}")

invocar_clones("Naruto A", "Naruto B")
invocar_clones("Naruto A", "Naruto B" , "Naruto C" , "Naruto D" , "Naruto E")


vila = "Vila da folha"

def missao():
    rank = "Missão Rank A"
    print (f"Vila: {vila}")
    print (f"Tipo: {rank}")

missao()
print(f"Vila {vila}")
