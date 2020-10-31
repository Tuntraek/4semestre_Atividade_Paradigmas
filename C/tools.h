#ifndef TOOLS
#define TOOLS

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "atleta.h"
#include <stdbool.h>

#define MAX_INPUT 10

_Bool validateName(atleta *);
void getplayername(atleta *);
void printmainmenu();
void printendmessage();
void getinput(char *, char *);
void getint(int *);
void getdouble(double *);
int compare_doubles(const void *a, const void *b);
char * upperTolower(char *);
void printinvalidinput(char *);
#endif // TOOLS
