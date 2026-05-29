# 01
i = 0
while i < 20:
    i = i + 1
    print(f"Dedo Numero coletado {i}")

    print("Fim execução")


 #2 

while True:
    palavra = input("Digite uma palavra ")
    if palavra == "Expansão de Domínio":
        break

 # 3
while soma <= 100:
    numero = float(input("Digite um numero: "))
    soma = soma + numero

    print("A soma final é: ", soma)
# 04
senha_correta = "naosei"
tentativas = 3

while tentativas > 0:
    digiteSenha = input("Digite a senha ")

    if digiteSenha == senha_correta :
        print("Pergaminho aberto")
        break
    else:
        tentativas -= 1
        if tentativas >0:
            print("Senha incorreta, restantes {tentativas}")
else:
    print("Tentativas espiradas")

    # 05
import random

energia = 0
while True:
    valor = random.randint(1, 5)
    energia += valor
    print(f"Adicionou {valor} de energia. Energia atual: {energia}")
    if energia == 7:
        print("BLACK FLASH ativado com precisão!")
        break
    elif energia > 15:
        print("Energia excedeu o limite! Ataque falhou.")
        break

    # final
hp_jogador = 50
hp_inimigo = 50

while hp_jogador > 0 and hp_inimigo > 0 :
    meuAtaque = int(input("Qual é o valor do seu ataque (5-10)"))
    hp_inimigo = hp_inimigo - meuAtaque
    hp_jogador = hp_jogador - 7
    print(f"Vida neste round: {hp_jogador}")
    print(f"O HP do adversario é de {hp_inimigo}")


if hp_jogador <= 0:
     print("Voce perdeu!")
elif hp_inimigo <= 0:
    print("Voce ganhou ")
elif hp_inimigo == 0 and hp_jogador == 0 :
    print("Deu empate!") 