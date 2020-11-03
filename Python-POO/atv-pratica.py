import os
import time

'''
ATIVIDADE PRATICA  - PARADIGMAS DE PROGRAMAÇÃO

EVAIR MARINHO
HENRIQUE CAMARGO
GUILHERME MAIURI GATTI

'''

# Classe com métodos de validação de int, float e somente letras
class Validador:
    # Validador para Int
    def Int(self, n):
        try:
            n = int(input())
            return n
        except:
            print('---------------------------')
            print('Entrada inválida, apenas números inteiros!')
            print('Digite novamente')
            print('---------------------------')
            time.sleep(2)
            return False

    # Validador para Float
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

    # Classe auxiliar da Input - Retorna True se a String conter somente letras
    def Alpha(self, nome):
        return str(nome).isalpha()

    # Valida um input de String do usuário para aceitar somente letras no input
    def Input(self, nome):
        nome = input()
        while not self.Alpha(nome):
            print('Digite novamente - apenas caracteres')
            nome = input()

        return nome

# Classe básica para jogador
class Jogador:
    def __init__(self, nome):
        self.__nome = nome

    # Retorna o nome do jogador
    def getNome(self):
        return self.__nome

# Classe JogadorGinastica herdando clase Jogador
class JogadorGinastica(Jogador):
    def __init__(self, nome):
        self.__notas = ['','','','','']
        super().__init__(nome)
    # Método que retorna a lista com as notas
    def getNotas(self):
        return self.__notas

    def setNotas(self, notas):
        self.__notas = notas

#Classe básica para jogo
class Jogo:
    def __init__(self, jog1, jog2):
        self.__jog1 = jog1
        self.__jog2 = jog2

# Classe Ginastica herdando a classe Jogo
class Ginastica(Jogo):

    def __init__(self, jog1, jog2):
        super().__init__(jog1, jog2)

    # Método para pegar o input de notas e setar no atributo de pontuação
    def inputNotas(self, jog):
        validador = Validador()
        cont = 0
        pontuacao = jog.getNotas()
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

            jog.setNotas(pontuacao)
            cont = cont + 1
        print('---------------------------')

    # Método que calcula a nota final de cada jogador e a retorna.
    def calcPontuacao(self, jog):
        notas = jog.getNotas()
        notas = sorted(notas)
        total = int(0)
        contBaixa = 0

        for i in notas:
            total = sum(notas) - notas[0]

        return int(total)
        
    # Método que define o ganhador da partida, mostrando uma mensagem personalizada
    def ganhador(self, jogo, jog1, jog2):
        print('Nota do Jogador 1 '+jog1.getNome()+': '+str(jogo.calcPontuacao(jog1)))
        print('Nota do Jogador 2 '+jog2.getNome()+': '+str(jogo.calcPontuacao(jog2)))
        print('---------------------------')

        if int(jogo.calcPontuacao(jog1)) > int(jogo.calcPontuacao(jog2)):
            print('Parabéns, '+jog1.getNome()+', você venceu!')
        elif int(jogo.calcPontuacao(jog1)) == int(jogo.calcPontuacao(jog2)):
            print("Empate entre "+jog1.getNome()+' e '+jog1.getNome())
        else:
            print('Parabéns, '+jog2.getNome()+', você venceu!')

    # Método que inicia todo o jogo de Ginastica e termina o mesmo baseado na escolha do usuário ao final da partida
    def iniciarJogo(self, jog1, jog2):
        partida = 1
        val = Validador()

        while(partida == 1):
            print("+---------------------------+\n" +
                  "|   Dois atletas competem   |\n" +
                  "|   e recebem 5 pontuações  |\n" +
                  "|    cada. Descarta-se a    |\n" +
                  "|   menor nota. Compara-se  |\n" +
                  "|   a soma das notas para   |\n" +
                  "|    declarar o vencedor.   |\n" +
                  "+---------------------------+\n" +
                  " ENTER para continuar...")
            entrada = input()
            jogo = Ginastica(jog1, jog2)
            jogo.inputNotas(jog1)
            jogo.inputNotas(jog2)
            jogo.ganhador(jogo, jog1, jog2)
            print('Jogar mais uma partida? (1 sim - 0 não)')
            partida = val.Int(partida)
            os.system("cls")
        os.system("cls")

        main()
        print('---------------------------')

# Classe JogadorArremesso herdando a classe Jogador
class JogadorArremesso(Jogador):

    def __init__(self, nome):
        self.__arremessos = []
        super().__init__(nome)

    # Adiciona arremessos do jogador no atributo que os armazena
    def setArremesso(self, arremesso):
        self.__arremessos.append(arremesso)
    
    #Retorna os arremessos do jogador
    def getArremessos(self):
        return self.__arremessos

# Classe Arremesso herdando a classe jogo
class Arremesso (Jogo):
    
    def __init__(self, jog1, jog2):
        super().__init__(jog1, jog2)

    #Método para o jogador realizar os arremessos, retornando todos os arremessos do jogador
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
                jog.setArremesso(arremesso)
                arremessos=jog.getArremessos()
                arremessos=sorted(arremessos)
            cont += 1
        return arremessos

    # Método que define o ganhador da partida, mostrando uma mensagem personalizada
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

    # Método que inicia todo o jogo de Arremesso e termina o mesmo baseado na escolha do usuário ao final da partida
    def iniciarJogo(self,jog1,jog2):
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
                  "|     maior distância.      |\n" +
                  "+---------------------------+\n" +
                  " ENTER para continuar...")
            entrada = input()
            jogo = Arremesso(jog1, jog2)
            jogo.ganhador(jogo, jog1, jog2)
            print('Jogar mais uma partida? (1 sim - 0 não)')
            partida = val.Int(partida)
            os.system("cls")
        os.system("cls")
        main()

# Função principal do programa
def main():
    val = Validador()
    opcao = '' 
    menu()
    opcao = val.Int(opcao)

    #Ginástica artística
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
    #Arremesso de peso
    elif opcao == 2:
        print('Digite o nome do jogador 1')
        j1 = ''
        j1 = val.Input(j1)
        print('Digite o nome do jogador 2')
        j2 = ''
        j2 = val.Input(j2)
        jog1Arremesso = JogadorArremesso(j1)
        jog2Arremesso = JogadorArremesso(j2)
        arremesso = Arremesso(jog1Arremesso, jog2Arremesso)
        arremesso.iniciarJogo(jog1Arremesso, jog2Arremesso)

    elif opcao == 3:
        breakpoint

    else:
        print('Opção inexistente no menu')
        time.sleep(2.5)
        os.system("cls")
        main()

# Menu principal do usuário
def menu():
    print("----COMPETIÇÕES ESPORTIVAS----\n")
    print("Digite uma opção\n")
    print("1 - Ginástica artística")
    print("2 - Arremesso de peso")
    print("3 - Sair do jogo")

#Chamada da main
main()
