import os
import time
    
class Validador:
    def validador(self,n):
        try:
            n = int(input())
            return n
        except:
            print('Entrada inválida!')
            time.sleep(4)
            os.system("cls")
            main()
            Validador.validador(n)

class Jogador:
    def __init__ (self,nome):
        self.__nome = nome
        self.__pontuacao=[1,1,1,1,1]
    def getNome(self):
        return self.__nome
    def getPontuacao(self):
        return self.__pontuacao
    def setPontuacao(self,pontuacao):
        self.__pontuacao=pontuacao

class Jogo:
    def __init__(self,jog1,jog2):
        self.__jog1=jog1
        self.__jog2=jog2

class Ginastica(Jogo):
    def __init__(self,jog1,jog2):
        super().__init__(jog1,jog2)

    def nota(self,jog):
        cont = 0
        pontuacao = jog.getPontuacao()
        print('---------------------------')
        print('Jogador '+jog.getNome())
        while(cont<5):
            print('Digite a nota '+str(cont+1))
            pontuacao[cont] = input()

            jog.setPontuacao(pontuacao)   
            cont = cont + 1
        print('---------------------------')

    def iniciarJogo(self,jog1,jog2):
        jogo = Ginastica(jog1,jog2)
        jogo.nota(jog1)
        jogo.nota(jog2)
        jogo.ganhador(jogo,jog1,jog2)
                
    def calcNota(self,jog):
        pontuacao = jog.getPontuacao()
        baixa = pontuacao[0]
        for i in pontuacao:
            if i<baixa:
                baixa = i
        total=0
        for i in pontuacao:
            if not(i == baixa):
                total+=int(i)
        return total

    def ganhador(self,jogo,jog1,jog2):
        if int(jogo.calcNota(jog1))>int(jogo.calcNota(jog2)):
            print('Nota do Jogador 1 '+jog1.getNome()+': '+str(jogo.calcNota(jog1)))
            print('Nota do Jogador 2 '+jog2.getNome()+': '+str(jogo.calcNota(jog2)))
            print('---------------------------')
            print('Parabéns '+jog1.getNome()+'!')
        elif jogo.calcNota(jog1)<jogo.calcNota(jog2):
            print('Nota do Jogador 1 '+jog1.getNome()+': '+str(jogo.calcNota(jog1)))
            print('Nota do Jogador 2 '+jog2.getNome()+': '+str(jogo.calcNota(jog2)))
            print('---------------------------')
            print('Parabéns '+jog2.getNome()+'!')
def main():
    menu() 
    opcao = 0
    validador = Validador()
    opcao = validador.validador(opcao)
    if opcao == 1:
        print('Digite o nome do jogador 1')
        j1=input()
        print('Digite o nome do jogador 2')
        j2=input()
        jog1Gin=Jogador(j1)
        jog2Gin=Jogador(j2)
        ginastica=Ginastica(jog1Gin,jog2Gin)
        ginastica.iniciarJogo(jog1Gin,jog2Gin)
        main()
    elif opcao == 2 :
        main()
    elif opcao == 3:
        breakpoint
    
    
def menu():
    print("----COMPETIÇÕES ESPORTIVAS----\n")
    print("Digite uma opção\n")
    print("1 - Ginástica artística")
    print("2 - Arremeso de peso")
    print("3 - Sair do jogo")
main()