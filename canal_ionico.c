#include <stdio.h>
#include <stdlib.h>
/*Main*/
int main()
{
    int lineas = 0;
    int i;
    char ch;
    FILE *datos;
    /*Contar el numero de lineas del archivo*/
    datos = fopen("Canal_ionico.txt", "r");
    while(!feof(datos))
    {
        ch = fgetc(datos);
        if(ch == '\n'){
            lineas++;
        }
    }
    fclose(datos);
    /*Arryas que guardan las coordenadas de los puntos*/
    double *coordenadasX;
    coordenadasX = malloc(num_lineas*sizeof(double));
    double *coordenadasY;
    coordenadasY = malloc(num_lineas*sizeof(double));
    /*Cargas los datos a los arrays creados*/
    double x,y;
    datos = fopen ("Canal_ionico.txt", "r");
    for(i=0;i<lineas;i++){
        if(datos == null){
            printf("No se encuentra el arhcivo, o no existe");
        }else{
            fscanf(datos, "%f %f",&x,&y);
            arrayX[i] = x;
            arrayY[i] = y; 
        }
    }    
    fclose(datos);
    /*Imprimir los datos que se guardaron en los arrays*/
    for(i=0;i<num_lineas;i++){
        printf("%f %f\n", coordenadasX[i], coordenadasY[i]);
    }
    
    return 0;
}