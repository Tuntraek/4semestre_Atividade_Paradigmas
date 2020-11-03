#include "main.h"

int main(){

    int option = 0;
    while(option != 3){

        printmainmenu();

        getint(&option);

        switch(option){
            case 1:
                arremessoinit();
                break;
            case 2:
                ginasticaartisticainit();
                break;
            case 3:
                printendmessage();
                break;
            default:
                printinvalidinput("** Opcao errada **", 1000);
                break;
        }
    }

    return 0;
}
