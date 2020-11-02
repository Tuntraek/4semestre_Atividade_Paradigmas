#ifndef GINASTICAARTISTICA
#define GINASTICAARTISTICA

#include "tools.h"

void ginasticaartisticainit();
void printginasticamenu();
void ginasticaplayerturn(atleta *, double *);
void ginasticacalculatehighscore(atleta *, double *);
void printginasticawinner(atleta *);
atleta * setginasticawinner(atleta *, atleta *,double ,double );

#endif
