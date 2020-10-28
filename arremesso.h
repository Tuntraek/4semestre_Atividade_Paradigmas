#ifndef ARREMESSO
#define ARREMESSO

#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <windows.h>

#include "atleta.h"
#include "tools.h"

enum JOGARNOVAMENTE{
    NAO,
    SIM,
};

void printarremessomenu();
enum JOGARNOVAMENTE arremessoinit();
void calculatehighscore(atleta*);
void getplayername(atleta*);
void playerturn(atleta* );
void printwinner(atleta* );
atleta* setwinner(atleta* , atleta* );
int playagain();

#endif // ARREMESSO
