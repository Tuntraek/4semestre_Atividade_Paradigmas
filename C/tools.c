#include "tools.h"

void getplayername(atleta *atleta_){
    char *nome = NULL;
    size_t len;
    char message[50];
    static int numero_jogador = 1;

    while(TRUE){
        sprintf(message, "Primeiro nome do atleta #%d: ", numero_jogador);
        getinput(atleta_->nome, message);
        nome = atleta_->nome;

        len = strlen(nome);
        if (len > 0 && validateName(atleta_))
            break;
        printinvalidinput("** Nome invalido. **");
    }

    if(nome[len-1] == '\n'){
        nome[len-1] = '\0';
    }
    numero_jogador++;
}

_Bool validateName(atleta * atleta_){
    int i = 0;
    char *letra = &(atleta_->nome);
    while(*letra != '\0'){
        if( (int) *(letra+i) < 65   ||
          ( (int) *(letra+i) > 90   &&
            (int) *(letra+i) < 97 ) ||
            (int) *(letra+i) > 122   )
        {
            return false;
        } else {
            if(*(letra+i+1) == '\0')
                return true;
            else
                i++;
        }
    }
}

void printinvalidinput(char *message){
    system("cls");
    fputs(message, stdout);
    Sleep(1000);
    system("cls");
}

void printloadingresult(){
    fputs("Calculando resultado", stdout);
    Sleep(500);
    for(int i=0; i<3; ++i){
        fputs(".", stdout);
        Sleep(500);
    }
    system("cls");
    Sleep(400);
}

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
    Sleep(2000);
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

int compare_doubles (const void *a, const void *b) {
  const double *da = (const double *) a;
  const double *db = (const double *) b;

  return (*da < *db) - (*da > *db);
}
