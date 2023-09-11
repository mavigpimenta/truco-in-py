import random
import time


def jogadores():
    print("Digite o nome do Jogador")
    print(">" ,end="")
    User1 = input().capitalize()
    return User1


class Carta:
    def __init__(self, _nome, _numero):
        self.nome = _nome
        self.numero = _numero


def criar_baralho():
    global baralho, cartavira 
    baralho = [Carta("Três de Paus", 10), Carta("Três de Copas", 10), Carta("Três de Espadas", 10), Carta("Três de Ouro", 10),
               Carta("Dois de Paus", 9), Carta("Dois de Copas", 9), Carta("Dois de Espadas", 9), Carta("Dois de Ouro", 9),
               Carta("As de Paus", 8), Carta("As de Copas", 8), Carta("As de Espadas", 8), Carta("As de Ouro", 8),
               Carta("Rei de Paus", 7), Carta("Rei de Copas", 7), Carta("Rei de Espadas", 7), Carta("Rei de Ouro", 7),
               Carta("Valete de Paus", 6), Carta("Valete de Copas", 6), Carta("Valete de Espadas", 6), Carta("Valete de Ouro", 6),
               Carta("Dama de Paus", 5), Carta("Dama de Copas", 5), Carta("Dama de Espadas", 5), Carta("Dama de Ouro", 5),
               Carta("Sete de Paus", 4), Carta("Sete de Copas", 4), Carta("Sete de Espadas", 4), Carta("Sete de Ouro", 4),
               Carta("Seis de Paus", 3), Carta("Seis de Copas", 3), Carta("Seis de Espadas", 3), Carta("Seis de Ouro", 3),
               Carta("Cinco de Paus", 2), Carta("Cinco de Copas", 2), Carta("Cinco de Espadas", 2), Carta("Cinco de Ouro", 2),
               Carta("Quatro de Paus", 1), Carta("Quatro de Copas", 1), Carta("Quatro de Espadas", 1), Carta("Quatro de Ouro", 1),]
    
    cartavira = baralho[random.randint(0, len(baralho)-1)]
    baralho.remove(cartavira)

    if cartavira.numero == 10:
        for i in baralho:
            if i.numero == 1:
                if "Paus" in i.nome:
                    i.numero += 100
                elif "Copas" in i.nome:
                    i.numero += 99
                elif "Espadas" in i.nome:
                    i.numero += 98
                elif "Espadas" in i.nome:
                    i.numero += 97
                elif "Ouro" in i.nome:
                    i.numero += 96
    else:
        for i in baralho:
            if i.numero == cartavira.numero + 1:
                if "Paus" in i.nome:
                    i.numero += 100
                elif "Copas" in i.nome:
                    i.numero += 99
                elif "Espadas" in i.nome:
                    i.numero += 98
                elif "Espadas" in i.nome:
                    i.numero += 97
                elif "Ouro" in i.nome:
                    i.numero += 96
        

def usercarta():
    carta_num = random.randint(0, len(baralho)-1)
    carta = baralho[carta_num]
    baralho.remove(baralho[carta_num])
    return carta


def pccarta():
    carta_num = random.randint(0, len(baralho)-1)
    carta = baralho[carta_num]
    baralho.remove(baralho[carta_num])
    return carta


def jogo():
    UserPoints = 0
    PCPoints = 0
    player = jogadores()
    
    def placar():
        print(f"\n{player}: {UserPoints} | PC: {PCPoints}\n")
        time.sleep(1)
    placar()
    
    while UserPoints < 12 and PCPoints < 12:
        criar_baralho()
        UserRoundPoints = 0
        PCRoundPoints = 0
        Rounds = 1
        playedCards = []
        valueRd = 1
        
        print("A rodada irá começar...")
        time.sleep(1)
        print(f"Virou a carta {cartavira.nome}")

        MaoUser = [usercarta(), usercarta(), usercarta()]
        MaoPc = [pccarta(), pccarta(), pccarta()]
        time.sleep(2)
        
        print(f"\nEssa é sua mão {MaoUser[0].nome, MaoUser[1].nome, MaoUser[2].nome}")
        time.sleep(1)
        
        print("Você gostaria de pedir Truco?")
        resposta = input().lower()
        if resposta.startswith("s"):
            print("O PC aceita o Truco?") 
            replyPC = random.randint(0, 1)
            if replyPC == 1:
                valueRd += 2
                print("Sim")
                time.sleep(1)
            else:
                print("Não")
                time.sleep(1)
        else:
            trucoPC = random.randint(0,1)
            if trucoPC == 1:
                print("O PC quer pedir truco, você aceita?")
                replyTruco = input().lower()
                if replyTruco.startswith("s"):
                    valueRd += 2
                else:
                    pass
            
        while UserRoundPoints < 2 and PCRoundPoints < 2 and Rounds < 4:
            UserPlay = int(input("\nQual carta você deseja jogar?"))
            while UserPlay < 0 or UserPlay > 2 or UserPlay in playedCards:
                print("Escolha uma carta presente em sua mão!\n")
                UserPlay = int(input("Qual carta você deseja jogar?"))
                
            chosenCard = MaoUser[UserPlay]
            playedCards.append(UserPlay)
            
            print(f"\nVocê jogou {MaoUser[UserPlay].nome}")
            time.sleep(1)
            print(f"PC jogou {MaoPc[Rounds - 1].nome}")
            time.sleep(1)
        
            if chosenCard.numero > MaoPc[Rounds - 1].numero:
                print("\nVocê ganhou esse Round")
                UserRoundPoints += 1 + ((4 - Rounds) / 10) 
                time.sleep(2)
            elif chosenCard.numero == MaoPc[Rounds - 1].numero:
                print("\nEsse Round embuxou")
                time.sleep(2)
                if chosenCard.numero > MaoPc[Rounds - 1].numero and UserRoundPoints > PCRoundPoints:
                    break
                elif chosenCard.numero < MaoPc[Rounds - 1].numero and UserRoundPoints < PCRoundPoints:
                    break
            else:
                print("\nO PC ganhou esse Round")
                PCRoundPoints += 1 + ((4 - Rounds) / 10)
                time.sleep(2)
            Rounds += 1
               
        if UserRoundPoints > PCRoundPoints:
            print("\nVocê ganhou essa Rodada")
            UserPoints += 1
            if valueRd == 3:
                UserPoints += 2
            
        else:
            print("\nO PC ganhou essa Rodada")
            PCPoints += 1
            if valueRd == 3:
              PCPoints += 2 
        placar()      
        
    if UserPoints >= 12:
        print("Você ganhou o jogo!")
    elif PCPoints >= 12:
        print("O PC ganhou o jogo!")
       
jogo()
