#include <stdio.h>
#include <stdlib.h>
/*Main*/
int main(void)
{
    int lineas = 0;
    int i;
    char ch;
    FILE *datos;
    /*Contar el numero de lineas del archivo*/
    datos = fopen("Canal_ionico.txt", "r");
    if(!datos){
        printf("Problemas con el archivo");
    }else{
        ch = fgetc(datos);
        if(ch == '\n'){
            lineas++;
        }
    }
    fclose(datos);
    /*Arrays que guardan las coordenadas de los puntos*/
    double *coordenadasX;
    coordenadasX = malloc(lineas*sizeof(double));
    double *coordenadasY;
    coordenadasY = malloc(lineas*sizeof(double));
    /*Carga los datos a los arrays creados*/
    double x,y;
    datos = fopen ("Canal_ionico.txt", "r");
    for(i=0;i<lineas;i++){
        if(!datos){
            printf("Problemas con el archivo");
        }else{
            fscanf(datos, "%f %f\n",&x,&y);
            coordenadasX[i] = x;
            coordenadasY[i] = y; 
        }
    }    
    fclose(datos);
    /*Imprimir los datos que se guardaron en los arrays*/
    for(i=0;i<lineas;i++){
        printf("%f %f\n", coordenadasX[i], coordenadasY[i]);
    }
    return 0;
}