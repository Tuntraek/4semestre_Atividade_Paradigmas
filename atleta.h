#ifndef ATLETA
#define ATLETA

#define MAX_NAME_SIZE 50

typedef struct atleta{
    char nome[MAX_NAME_SIZE];
    double pontuacao[3];
    double highscores[3];
} atleta;

#endif // ATLETA
