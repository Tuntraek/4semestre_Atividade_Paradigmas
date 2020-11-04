#include "ginasticaArtistica.h"


void ginasticaartisticainit(){
    printginasticamenu();

    atleta *atleta1 = malloc(sizeof(atleta));
    atleta *atleta2 = malloc(sizeof(atleta));
    double totalAtleta1 = 0.f;
    double totalAtleta2 = 0.f;

    ginasticaplayerturn(atleta1, &totalAtleta1, 1);
    ginasticaplayerturn(atleta2, &totalAtleta2, 2);

    printginasticawinner(setginasticawinner(atleta1, atleta2, totalAtleta1, totalAtleta2));
}

atleta* setginasticawinner(atleta * atleta1, atleta * atleta2, double total1, double total2){

    if(total1 == total2){
        //NULL indica empate.
        return NULL;
    }else if (total1 > total2)
        return atleta1;
    else
        return atleta2;
}

void printginasticawinner(atleta* atleta){

    printloadingresult();

    char message[100];

    if(!atleta)
        fputs("Empate!!", stdout);
    else{
        sprintf(message, "Atleta %s venceu!!", atleta->nome);
        fputs(message, stdout);
    }
    Sleep(3000);
    system("cls");
}

void ginasticaplayerturn(atleta *atleta_, double * pontuacaoTotal, int numeroJogador){

    getplayername(atleta_, numeroJogador);
    system("cls");

    for(int i=0; i < 5; i++){

        fprintf(stdout, "Atleta %s \n"   , atleta_->nome );
        fprintf(stdout, "%d# nota: ", i+1           );

        getdouble(&atleta_->pontuacao[i]);

        double ponto = atleta_->pontuacao[i];

        if( ponto > 10  ||
            ponto < 0.f ||
            ponto == -1000 ){
            printinvalidinput("Valor entre 0 e 10!", 1000);
            i--;
        }
        system("cls");
    }

    ginasticacalculatehighscore(atleta_, pontuacaoTotal);

    system("cls");

}

#define NUMEROPONTOS 5

void ginasticacalculatehighscore(atleta *atleta_, double * pontuacaoTotal){
    for(int i = 0; i < NUMEROPONTOS; i++){
        atleta_->highscores[i] = atleta_->pontuacao[i];
    }
    qsort(&atleta_->highscores, NUMEROPONTOS, sizeof(double), compare_doubles);

    //zera menor pontuação
    atleta_->highscores[NUMEROPONTOS-1] = 0;

    //faz somátoria dos pontos totais
    for(int i = 0; i < NUMEROPONTOS-1; i++){
        *pontuacaoTotal += atleta_->highscores[i];
    }
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
