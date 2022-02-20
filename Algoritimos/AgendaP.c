#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
struct Cadastro
{
    char *Nome;
    char *Telefone;
    char *Cidade;
    char *endereco;
    char *estado;
    char *nascimento;
};

void searchmodify (int C, struct Cadastro Agenda[]){
    char StrgBusca[20],StrgBuscaUP[20];
    int i,Resultado,selector;
    while (selector !=-1){
        printf("Insira o nome aqui : ");
        scanf("%[^\n]s",StrgBusca);
        setbuf(stdin, NULL);  
        selector=-2;
        int Resultado1 =0;
        for (i = 0; i < C; i++)
        {
            Resultado=strcmp(Agenda[i].Nome,StrgBusca);
            
            if(Resultado == 0)
            {
            Resultado1+=1;
            printf("NOME         TELEFONE         ENDEREÇO         CIDADE         ESTADO         NASCIMENTO         COD \n");
            printf("%s         ",Agenda[i].Nome);
            printf("%s         ",Agenda[i].Telefone);
            printf("%s         ",Agenda[i].endereco);
            printf("%s         ",Agenda[i].Cidade);
            printf("%s         ",Agenda[i].estado);
            printf("%s         ",Agenda[i].nascimento);
            printf("%d \n",i);
            }
            else
            {

            }
        }
        if (Resultado1 ==0)
        {
            printf("SEM RESULTADOS \n");
        }
        else
        {
            printf("Insira o Código para Modificar (Se for -1, sairá da ferramenta) : ");
            scanf("%d",&selector);
            setbuf(stdin, NULL);  

            if (selector <=0 && selector<C){
                addnew(selector,Agenda);
            }
            else
            {
                printf("COD NÃO DEFINIDO");
            }
            

        }
        printf("Deseja nova busca: (-1) para não,()");
        scanf("%d",&selector);
        setbuf(stdin, NULL);  



        
    }
    printf("\n");
}

void printall (int C, struct Cadastro Agenda[]){
      printf("NOME--------------TELEFONE-------------ENDEREÇO------------CIDADE----------ESTADO------NASCIMENTO \n");

    for(int i=0;i<C;i++){
        printf("%s         |",Agenda[i].Nome);
        printf("%s         |",Agenda[i].Telefone);
        printf("%s         |",Agenda[i].endereco);
        printf("%s         |",Agenda[i].Cidade);
        printf("%s         |",Agenda[i].estado);
        printf("%s         |\n",Agenda[i].nascimento);


}
}

void addnew (int C, struct Cadastro Agenda[]){
    char aux[100],auxup[100];
    int tam,i;
    
    printf("Insira o nome : ");
    scanf("%[^\n]s",aux);
    tam = strlen(aux);
    Agenda[C].Nome = (char *) malloc(tam*sizeof(char));
    setbuf(stdin, NULL);  
    for (i = 0; i < strlen(aux); i++)
    {
        auxup[i]=toupper(aux[i]);
    }
    strcpy(Agenda[C].Nome, auxup);
    memset (&aux, 0, sizeof (aux) );
    memset (&auxup, 0, sizeof (auxup) );

    printf("Insira o Telefone : ");
    scanf("%[^\n]s",aux);
    tam = strlen(aux);
    Agenda[C].Telefone = (char *) malloc(tam*sizeof(char));
    strcpy(Agenda[C].Telefone, aux);
    setbuf(stdin, NULL);
    memset (&aux, 0, sizeof (aux) );
    memset (&auxup, 0, sizeof (auxup) );

    printf("Insira o Endereço : ");
    scanf("%[^\n]s",aux);
    tam = strlen(aux);
    Agenda[C].endereco = (char *) malloc(tam*sizeof(char));
    setbuf(stdin, NULL);  
    for (i = 0; i < strlen(aux); i++)
    {
        auxup[i]=toupper(aux[i]);
    }
    strcpy(Agenda[C].endereco, auxup);
    memset (&aux, 0, sizeof (aux) );
    memset (&auxup, 0, sizeof (auxup) );
    
    printf("Insira a Cidade : ");
    scanf("%[^\n]s",aux);
    for (i = 0; i < strlen(aux); i++)
    {
        auxup[i]=toupper(aux[i]);
    }
    tam = strlen(aux);
    Agenda[C].Cidade = (char *) malloc(tam*sizeof(char));
    strcpy(Agenda[C].Cidade, auxup);
    setbuf(stdin, NULL);
    memset (&aux, 0, sizeof (aux) );
    memset (&auxup, 0, sizeof (auxup) );

    printf("Insira o Estado : ");
    scanf("%[^\n]s",aux);
    tam = strlen(aux);
    Agenda[C].estado = (char *) malloc(tam*sizeof(char));
    setbuf(stdin, NULL);  
    for (i = 0; i < strlen(aux); i++)
    {
        auxup[i]=toupper(aux[i]);
    }
    strcpy(Agenda[C].estado, auxup);
    memset (&aux, 0, sizeof (aux) );
    memset (&auxup, 0, sizeof (auxup) );

    printf("Insira o Nascimento (xx-xx-xxx): ");
    scanf("%[^\n]s",aux);
    tam = strlen(aux);
    Agenda[C].nascimento = (char *) malloc(tam*sizeof(char));
    setbuf(stdin, NULL);  
    for (i = 0; i < strlen(aux); i++)
    {
        auxup[i]=toupper(aux[i]);
    }
    strcpy(Agenda[C].nascimento, auxup);
    memset (&aux, 0, sizeof (aux) );
    memset (&auxup, 0, sizeof (auxup) );
}
int main (){
    int C=0;
    int capacidade = 3;
    struct Cadastro *Agenda;
    Agenda = (struct Cadastro *)malloc(sizeof(struct Cadastro)*capacidade);
    int select=-1;
    while (select!=0){
        printf("1) Cadastrar contato.\n");
        printf("2) Exibir contatos.\n");
        printf("3) Modificar Contado.\n");
        printf("0) Sair.\n");
        scanf("%d",&select);
        setbuf(stdin, NULL);

        if (select ==1){
            if(C < capacidade){
                addnew(C,Agenda);
                C++;
            }else{
                printf("Limite Atingido \n");
            }
            
        }
        if (select ==2 ){
            printall(C,Agenda);
        }
        if (select == 3){
            searchmodify(C,Agenda);
        }
    }

    return 0;
}
