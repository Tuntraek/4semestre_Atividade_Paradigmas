#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "tools.h"

void printinvalidinput(char *message){
    system("cls");
    fputs(message, stdout);
    sleep(1);
    system("cls");
}

char* upperTolower(char* str){
    int pos = 0;
    while(str[pos] != '\0' && ( (int)str[pos] < 90 && (int)str[pos] > 65) ){
        str[pos] = str[pos] + 32;
        pos++;
    }
    return str;
}

void getinput(char *value, char *prompt ){
    // prompt é um ou mais caracteres que aparecem no começo da linha para input
    fputs(prompt, stdout);

    // fgets pega o que o usuário escrever e põe em value
    if(fgets(value, MAX_INPUT, stdin)){

        char * newline;
        // checa se existe um newline
        if (newline = strchr(value, '\n'))
            *newline = 0;
        else{
            // scanf para limpar até o newline
            scanf("%*[^\n]");
            scanf("%*c");
        }

    }

    // scanf abandonado
    //scanf("%d", opt);
}

void getint(int *ival){
    // C string para input do usuario
    char value[MAX_INPUT] = "";
    getinput(value, "> ");

    // int temporario para pegar o inteiro da string
    int temp;

    // coloca um inteiro em temp se for encontrado em value
    if(sscanf(value, "%d", &temp))
        *ival = temp;
    else
        // qualquer valor inteiro para dar a mensagem de erro
        *ival = 4;
}

void getdouble(double *dval){
    // C string para input do usuario
    char value[MAX_INPUT] = "";
    getinput(value, " ");

    // double temporario para pegar o inteiro da string
    double temp;

    // coloca um inteiro em temp se for encontrado em value
    if(sscanf(value, "%lf", &temp))
        *dval = temp;
    else
        // qualquer valor double para dar a mensagem de erro
        *dval = 0;
}

int
compare_doubles (const void *a, const void *b)
{
  const double *da = (const double *) a;
  const double *db = (const double *) b;

  return (*da < *db) - (*da > *db);
}
