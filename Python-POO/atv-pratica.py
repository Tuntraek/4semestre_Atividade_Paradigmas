import os
import time

'''
ATIVIDADE PRATICA  - PARADIGMAS DE PROGRAMAÇÃO

EVAIR MARINHO
HENRIQUE CAMARGO
GUILHERME MAIURI GATTI

'''

##Classe com métodos de validação de int, float e somente letras
class Validador:
    #Validador de Int
    def Int(self, n):
        try:
            n = int(input())
            return n
        except:
            print('---------------------------')
            print('Entrada inválida!')
            print('Digite novamente')
            print('---------------------------')
            time.sleep(2)
            return False
    #Validador de Float
    def Float(self, n):
        try:
            n = float(input())
            return n
        except:
            print('---------------------------')
            print('Entrada inválida!')
            print('Digite novamente')
            print('---------------------------')
            time.sleep(2)
            return False

    #Classe auxiliar da Input - Retorna Truue se a String conter somente letras
    def Alpha(self, nome):
        return str(nome).isalpha()

    #Valida um input de String do usuário para aceitar somente letras no input
    def Input(self, nome):
        nome = input()
        while not self.Alpha(nome):
            print('Digite novamente - apenas caracteres')
            nome = input()

        return nome


class Jogador:
    def __init__(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
class JogadorGinastica(Jogador):
    def __init__(self, nome):
        self.__pontuacao = [int, int, int, int, int]
        super().__init__(nome)

    def getPontuacao(self):
        return self.__pontuacao

    def setPontuacao(self, pontuacao):
        self.__pontuacao = pontuacao


class Jogo:
    def __init__(self, jog1, jog2):
        self.__jog1 = jog1
        self.__jog2 = jog2


class Ginastica(Jogo):
    def __init__(self, jog1, jog2):
        super().__init__(jog1, jog2)

    def nota(self, jog):
        validador = Validador()
        cont = 0
        pontuacao = jog.getPontuacao()
        print('---------------------------')
        print('Jogador '+jog.getNome())
        while(cont < 5):

            pontuacao[cont] = False
            while (pontuacao[cont] == False):
                print('Digite a nota '+str(cont+1))
                pontuacao[cont] = validador.Int(pontuacao[cont])
                if(pontuacao[cont] < 0 or pontuacao[cont] > 10):
                    print('Nota de 0 a 10!')
                    pontuacao[cont] = False

            jog.setPontuacao(pontuacao)
            cont = cont + 1
        print('---------------------------')

    def iniciarJogo(self, jog1, jog2):
        partida = 1
        val = Validador()

        while(partida == 1):
            print("+---------------------------+\n" +
                  "|   Dois atletas competem   |\n" +
                  "|   e recebem 5 pontuacoes  |\n" +
                  "|    cada. Descarta-se a    |\n" +
                  "|   menor nota. Compara-se  |\n" +
                  "|   a soma das notas para   |\n" +
                  "|    declarar o vencedor.   |\n" +
                  "+---------------------------+\n" +
                  " ENTER para continuar...")
            entrada = input()
            jogo = Ginastica(jog1, jog2)
            jogo.nota(jog1)
            jogo.nota(jog2)
            jogo.ganhador(jogo, jog1, jog2)
            print('Jogar mais uma partida? (1 sim - 0 não)')
            partida = val.Int(partida)
            while partida != 1 and partida != 0:
                print('Apenas 1 ou 0')
                partida = val.Int(partida)
            os.system("cls")
        os.system("cls")
        main()

    def calcNota(self, jog):
        pontuacao = jog.getPontuacao()
        pontuacao = sorted(pontuacao)
        total = int(0)
        contBaixa = 0
        for i in pontuacao:
            total = sum(pontuacao) - pontuacao[0]

        return int(total)

    def ganhador(self, jogo, jog1, jog2):
        print('Nota do Jogador 1 '+jog1.getNome()+': '+str(jogo.calcNota(jog1)))
        print('Nota do Jogador 2 '+jog2.getNome()+': '+str(jogo.calcNota(jog2)))
        print('---------------------------')
        if int(jogo.calcNota(jog1)) > int(jogo.calcNota(jog2)):
            print('Parabéns, '+jog1.getNome()+', você venceu!')
        elif int(jogo.calcNota(jog1)) == int(jogo.calcNota(jog2)):
            print("Empate entre "+jog1.getNome()+' e '+jog1.getNome())
        else:
            print('Parabéns, '+jog2.getNome()+', você venceu!')

        print('---------------------------')


class Arremesso (Jogo):
    def __init__(self, jog1, jog2):
        super().__init__(jog1, jog2)

    def iniciarJogo(self, jog1, jog2):
        partida = 1
        val = Validador()
        while(partida == 1):
            print("+---------------------------+\n" +
                  "|   Dois atletas competem   |\n" +
                  "|   e possuem 3 arremessos  |\n" +
                  "|  cada. Vence quem possuir |\n" +
                  "|   a maior distancia. Em   |\n" +
                  "|   caso de empate, vence   |\n" +
                  "|   quem tiver a proxima    |\n" +
                  "|     maior distancia.      |\n" +
                  "+---------------------------+\n" +
                  " ENTER para continuar...")
            entrada = input()
            jogo = Arremesso(jog1, jog2)
            jogo.ganhador(jogo, jog1, jog2)
            print('Jogar mais uma partida? (1 sim - 0 não)')
            partida = val.Int(partida)
            while partida != 1 and partida != 0:
                print('Apenas 1 ou 0')
                partida = val.Int(partida)
            os.system("cls")
        os.system("cls")
        main()

    def arremessar(self, jog):
        val = Validador()
        cont = 0
        arremessos = []
        
        print('Jogador '+jog.getNome())
        while (cont < 3):
            arremesso = False
            while (arremesso == False):
                print('Arremesso '+str(cont+1))
                arremesso = val.Float(arremesso)
            if arremesso != False:
                arremessos.append(arremesso)
                arremessos = sorted(arremessos)
            cont += 1
        return arremessos

    def ganhador(self, jogo, jog1, jog2):
        print('---------------------------')
        arremesosJog1 = jogo.arremessar(jog1)
        arremesosJog2 = jogo.arremessar(jog2)
        print('Arremessos do jogador '+jog1.getNome()+' '+str(arremesosJog1))
        print('Arremessos do jogador '+jog2.getNome()+' '+str(arremesosJog2))
        if arremesosJog1[2] > arremesosJog2[2]:
            print('Parabéns, '+jog1.getNome()+', você venceu!')
        elif arremesosJog2[2] > arremesosJog1[2]:
            print('Parabéns, '+jog2.getNome()+', você venceu!')
        elif arremesosJog2[2] == arremesosJog1[2]:
            if arremesosJog1[1] > arremesosJog2[1]:
                print('Parabéns, '+jog1.getNome() +
                      ', você venceu com a segunda melhor nota!')
            elif arremesosJog2[1] > arremesosJog1[1]:
                print('Parabéns, '+jog2.getNome() +
                      ', você venceu com a segunda melhor nota!')
        else:
            print('Empate')


def main():
    val = Validador()
    opcao = 0
    while (opcao == 0):
        os.system("cls")
        menu()
        opcao = val.Int(opcao)

    if opcao == 1:
        print('Digite o nome do jogador 1')
        j1 = ''
        j1 = val.Input(j1)
        print('Digite o nome do jogador 2')
        j2 = ''
        j2 = val.Input(j2)
        jog1Gin = JogadorGinastica(j1)
        jog2Gin = JogadorGinastica(j2)
        ginastica = Ginastica(jog1Gin, jog2Gin)
        ginastica.iniciarJogo(jog1Gin, jog2Gin)
    elif opcao == 2:
        print('Digite o nome do jogador 1')
        j1 = ''
        j1 = val.Input(j1)
        print('Digite o nome do jogador 2')
        j2 = ''
        j2 = val.Input(j2)
        jog1Arremesso = Jogador(j1)
        jog2Arremesso = Jogador(j2)
        arremesso = Arremesso(jog1Arremesso, jog2Arremesso)
        arremesso.iniciarJogo(jog1Arremesso, jog2Arremesso)

    elif opcao == 3:
        breakpoint
    else:
        print('Opção inexistente no menu')
        time.sleep(2.5)
        os.system("cls")
        main()


def menu():
    print("----COMPETIÇÕES ESPORTIVAS----\n")
    print("Digite uma opção\n")
    print("1 - Ginástica artística")
    print("2 - Arremesso de peso")
    print("3 - Sair do jogo")


main()
