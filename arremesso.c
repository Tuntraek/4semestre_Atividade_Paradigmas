#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#include "arremesso.h"

#include "tools.h"

void printmenu(){
    system("cls");
    char *p;
    fputs("+---------------------------+\n"
          "|   Dois atletas competem   |\n"
          "|   e possuem 3 arremessos  |\n"
          "|  cada. Vence quem possuir |\n"
          "|   a maior distancia. Em   |\n"
          "|   caso de empate, vence   |\n"
          "|   quem tiver a segunda    |\n"
          "|     maior distancia.      |\n"
          "+---------------------------+\n"
          " ENTER para continuar...", stdout);
    getinput(p, "");
    sleep(1);
    system("cls");
}

void calculatehighscore(atleta *atleta_){

    qsort(&atleta_->pontuacao, 3, sizeof(double), compare_doubles);
    for(int i = 0; i < 3; i++){
        atleta_->highscores[i] = atleta_->pontuacao[i];
    }
}

void getplayername(atleta *atleta_){
    fputs("Nome do atleta: ", stdout);
    fgets(&atleta_->nome, MAX_NAME_SIZE, stdin );
    char *nome = &atleta_->nome;

    size_t len = strlen(nome);
    if(len > 0 && nome[len-1] == '\n'){
        nome[len-1] = '\0';
    }

}

void playerturn(atleta *atleta_){

    getplayername(atleta_);
    system("cls");

    for(int i=0; i < 3; i++){

        fprintf(stdout, "Atleta %s \n"   , &atleta_->nome );
        fprintf(stdout, "%d# Arremesso: ", i+1           );

        getdouble(&atleta_->pontuacao[i]);

        double ponto = atleta_->pontuacao[i];
        if( ponto == 0   ||
            ponto > 30.f ||
            ponto < -30.f  ){

            i--;
        }
        system("cls");
    }

    calculatehighscore(atleta_);

    sleep(2);
    system("cls");

}



void arremessoinit(){
    printmenu();

    atleta *atleta1 = malloc(sizeof(atleta));
    atleta *atleta2 = malloc(sizeof(atleta));


    playerturn(atleta1);
    playerturn(atleta2);

    //setwinner()
    if(atleta1)
        free(atleta1);
    if(atleta2)
        free(atleta2);

//    sleep(2);
//    system("cls");
}
