#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "tools.h"
#include "arremesso.h"

void printmainmenu(){
    fputs( "+-------------------------+\n"
           "|           MENU          |\n"
           "|                         |\n"
           "| 1 - Arremesso de peso   |\n"
           "| 2 - Ginastica Artistica |\n"
           "| 3 -       SAIR          |\n"
           "+-------------------------+\n", stdout);

}

void printendmessage(){
    system("cls");
    fputs("+-------------------------------+\n"
          "|                               |\n"
          "|      OBRIGADO POR USAR O      |\n"
          "|        NOSSO PROGRAMA!        |\n"
          "|                               |\n"
          "+-------------------------------+\n", stdout);
    sleep(3);
}

void printinvalidinput(){
    system("cls");
    fputs("** Opcao invalida **\n", stdout);
    sleep(1);
    system("cls");
}

int main()
{

    int option = 0;
    while(option != 3){

        printmainmenu();

        getint(&option);

        switch(option){
            case 1:
                arremessoinit();
                break;
            case 3:
                printendmessage();
                break;
            default:
                printinvalidinput();
                break;
        }
    }

    return 0;
}
