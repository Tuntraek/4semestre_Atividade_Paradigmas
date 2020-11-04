#ifndef ATLETA
#define ATLETA

#define MAX_NAME_SIZE 50

typedef struct atleta{
    char nome[MAX_NAME_SIZE];
    double pontuacao[5];
    double highscores[5];
} atleta;

#endif // ATLETA
