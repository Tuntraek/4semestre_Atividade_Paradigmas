#ifndef ARREMESSO
#define ARREMESSO

#include "tools.h"

void printarremessomenu();
void arremessoinit();
void arremessocalculatehighscore(atleta*);
void arremessoplayerturn(atleta* , int );
void printarremessowinner(atleta* );
atleta* setarremessowinner(atleta* , atleta* );


#endif // ARREMESSO
