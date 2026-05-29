hp = 0

while hp < 1 or  hp > 20 :
  hp = int(input ("Digite o HP (1-20) "))

if hp < 1 or hp > 20:
  print("Valor inválido! Tente novamente.")

print (f"HP: " , "❤️ " * hp)