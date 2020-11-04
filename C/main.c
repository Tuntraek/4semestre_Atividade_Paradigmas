#include "main.h"
/*
    PROJETO DO 4º SEMESTRE PARA PARADIGMAS DA PROGRAMAÇÃO

    Desenvolver um programa que simule dois jogos olímpicos,
    Arremesso de peso e ginástica olímpica.
    O programa apresenta um menu inicial para escolha dos jogos,
    para cada jogo, pede-se os nomes dos atletas e as pontuações,
    depois de tudo digitado, o programa calcula o resultado e
    apresenta para o usuário.

    Alunos involvidos:
    Nome: Guilherme Maiuri Gatti
    RA:   20838912
    Nome: Evair Marinho Vilas Boas Porfirio
    RA:   21051966
    Nome: Henrique Gonçalves Camargo
    RA:   21331824
*/

int main(){

    int option = 0;
    while(option != 3){

        printmainmenu();

        getint(&option);

        switch(option){
            case 1:
                arremessoinit();
                break;
            case 2:
                ginasticaartisticainit();
                break;
            case 3:
                printendmessage();
                break;
            default:
                printinvalidinput("** Opcao errada **", 1000);
                break;
        }
    }

    return 0;
}
