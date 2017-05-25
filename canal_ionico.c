#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*Declaracion de funciones*/
double calcularRadio(double x, double y);
double buscarRadioMaximo(double *X, double *Y, double rMolecula, int lineas, double centroX, double centroY);
/*Main*/
int main(void)
{
    int lineas = 0;
    int i;
    char ch;
    FILE *datos, *resultados;
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
            fscanf(datos, "%lf %lf\n",&x,&y);
            coordenadasX[i] = x;
            coordenadasY[i] = y; 
        }
    }    
    fclose(datos);
    /*Imprimir los datos que se guardaron en los arrays*/
    for(i=0;i<lineas;i++){
        printf("%lf %lf\n", coordenadasX[i], coordenadasY[i]);
    }
    double centroX, centroY, radioMax; /*Variables que guardan el centro del circulo maximo y su radio*/
    double radio_molecula = 1; /*Radio de la molecula en Angstroms*/
    /*Encontrar y guardar el radio maximo*/
    radioMax = buscarRadioMaximo(coordenadasX, coordenadasY, radio_molecula,  lineas, centroX, centroY);
    /*Exportar resultados al archivo "Resultados.txt"*/
    resultados = fopen("Resultados.txt","w");
    fprintf(resultados, "%lf\n", centroX);
    fprintf(resultados, "%lf\n", centroY);
    fprintf(resultados, "%lf\n", radioMax);
    for(i=0,i<lineas,i++){
        fprintf(resultados, "%lf %lf\n",coordenadasX[i], coordenadasY[i]);
    }
    fclose(resultados);
    return 0;    
}
/*Funcion que calculo la distancia entre dos puntos*/
double calcularRadio(double x, double y){
    double radio2;
    radio2 = (x*x + y*y);
    return pow(radio2, 0.5);
}
/*Funcion que busca el radio maximo y arroja los valores del centro del circulo*/
double buscarRadioMaximo(double *X, double *Y, double rMolecula, int lineas, double centroX, double centroY){
    int i,j;
    double radio, alpha, radio_max;
    double radio_incial = calcularRadio(X[0],Y[0]);/*Inicializar el radio*/
    for(i=1;i<lineas;i++){
        for(j=0;j<lineas;j++){
            radio = calcularRadio(X[i],Y[j]);
            alpha = radio/radio_inicial;
            if(alpha > 1){
                radio_max = radio-rMolecula;
                centroX = X[i];
                centroY = Y[j];
            }else{
                radio_max = radio_inicial-rMolecula;
                centroX = X[i-1];
                centroY = Y[j-1];
            }
            radio_inicial = radio;
        }
    }
    return radio_max;
}