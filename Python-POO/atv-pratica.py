import os
import time


class Validador:
    def Int(self, n):
        try:
            n = int(input())
            return n
        except:
            print('---------------------------')
            print('Entrada inválida!')
            print('Digite novamente')
            print('---------------------------')
            time.sleep(2.5)
            return 0

    def Float(self, n):
        try:
            n = float(input())
            return n
        except:
            print('---------------------------')
            print('Entrada inválida!')
            print('Digite novamente')
            print('---------------------------')
            time.sleep(2.5)
            return False

    def Alpha(self, nome):
        return str(nome).isalpha()

    def Input(self, nome):
        nome = input()
        while not self.Alpha(nome):
            print('Digite novamente - apenas caracteres')
            nome = input()

        return nome


class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__pontuacao = [int, int, int, int, int]

    def getNome(self):
        return self.__nome

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
            jogo = Ginastica(jog1, jog2)
            jogo.nota(jog1)
            jogo.nota(jog2)
            jogo.ganhador(jogo, jog1, jog2)
            print('Jogar mais uma partida? (1 sim - 0 não)')
            partida = val.Int(partida)
        main()

    def calcNota(self, jog):
        pontuacao = jog.getPontuacao()
        pontuacao=sorted(pontuacao)
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
        jog1Gin = Jogador(j1)
        jog2Gin = Jogador(j2)
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
        arremesso = Arremesso (jog1Arremesso, jog2Arremesso)

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
