#include "ginasticaArtistica.h"


void ginasticaartisticainit(){
    printginasticamenu();

    atleta *atleta1 = malloc(sizeof(atleta));
    atleta *atleta2 = malloc(sizeof(atleta));


}

void ginasticaplayerturn(atleta *atleta_){

    getplayername(atleta_);
    system("cls");

    for(int i=0; i < 3; i++){

        fprintf(stdout, "Atleta %s \n"   , atleta_->nome );
        fprintf(stdout, "%d# nota: ", i+1           );

        getdouble(&atleta_->pontuacao[i]);

        double ponto = atleta_->pontuacao[i];

        if( ponto > 10 ||
            ponto < 0.f  ){

            i--;
        }
        system("cls");
    }

    calculatehighscore(atleta_);

    system("cls");

}

void printginasticamenu(){
    system("cls");
    char p[10];
    fputs("+---------------------------+\n"
          "|   Dois atletas competem   |\n"
          "|   e recebem 5 pontuacoes  |\n"
          "|    cada. Descarta-se a    |\n"
          "|   menor nota. Compara-se  |\n"
          "|   a soma das notas para   |\n"
          "|    declarar o vencedor.   |\n"
          "+---------------------------+\n"
          " ENTER para continuar...", stdout);
    getinput(p, "");
    Sleep(300);
    system("cls");
}
