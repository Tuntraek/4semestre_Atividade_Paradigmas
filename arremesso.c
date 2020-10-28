#include "arremesso.h"



void printmenu(){
    system("cls");
    char p[10];
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
    Sleep(300);
    system("cls");
}

void calculatehighscore(atleta *atleta_){
    for(int i = 0; i < 3; i++){
        atleta_->highscores[i] = atleta_->pontuacao[i];
    }
    qsort(&atleta_->highscores, 3, sizeof(double), compare_doubles);
}

void getplayername(atleta *atleta_){
    char *nome = NULL;
    size_t len;

    while(TRUE){
        getinput(atleta_->nome, "Primeiro nome: ");
        nome = &atleta_->nome;

        len = strlen(nome);
        if (len > 0)
            break;
        printinvalidinput("** Nome invalido. **");
    }

    if(nome[len-1] == '\n'){
        nome[len-1] = '\0';
    }

}

void playerturn(atleta *atleta_){

    getplayername(atleta_);
    system("cls");

    for(int i=0; i < 3; i++){

        fprintf(stdout, "Atleta %s \n"   , atleta_->nome );
        fprintf(stdout, "%d# Arremesso: ", i+1           );

        getdouble(&atleta_->pontuacao[i]);

        double ponto = atleta_->pontuacao[i];

        if( ponto == 0   ||     //limitar a pontuação, record mundial masculino é de 23.12m...
            ponto > 30.f ||     //Valores negativos existem, o atleta pode ter arremessado para trás.
            ponto < -30.f  ){

            i--;
        }
        system("cls");
    }

    calculatehighscore(atleta_);

    system("cls");

}

atleta* setwinner(atleta *atleta1, atleta *atleta2){
    int i = 0;
    do {
        if(atleta1->highscores[i] == atleta2->highscores[i]){
            i++;
            break;
        } else if (atleta1->highscores[i] > atleta2->highscores[i])
            return atleta1;
        else
            return atleta2;
    } while (i != 2);
    return NULL;
}

void printwinner(atleta* atleta){

    fputs("Calculando resultado", stdout);
    Sleep(500);
    for(int i=0; i<3; ++i){
        fputs(".", stdout);
        Sleep(500);
    }
    system("cls");
    Sleep(400);

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

int playagain(){
    char resposta[10];
    while(TRUE){
        getinput(resposta, "Deseja jogar novamente?[sim/nao]");
        upperTolower(resposta);
        if(strcmp(resposta, "sim") == 0)
            return 1;
        else if (strcmp(resposta, "nao") == 0)
            return 0;
        else
            ;
    }

}

enum JOGARNOVAMENTE arremessoinit(){
    printmenu();

    atleta *atleta1 = malloc(sizeof(atleta));
    atleta *atleta2 = malloc(sizeof(atleta));


    playerturn(atleta1);
    playerturn(atleta2);

    printwinner(setwinner(atleta1, atleta2));

    if(atleta1)
        free(atleta1);
    if(atleta2)
        free(atleta2);

    return playagain();

}
