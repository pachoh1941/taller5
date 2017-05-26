#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*Declaracion de funciones*/
double calcularRadio(double x1, double x2, double y1, double y2, double radio_molecula);
/*Main*/
int main(void)
{
    int i;
    double centroX, centroY, radioMax; /*Variables que guardan el centro del circulo maximo y su radio*/
    double radio_molecula = 1; /*Radio de la molecula en Angstroms*/
    FILE *datos, *resultados,*puntos;
    /*Proceso de carga de los datos e iterciones para hallar la solucion*/
    double x,y,x1,y1,x2,y2;
    double radio, radio_inicial, alpha;
    /*Se inicializa radio_inicial arbitrariamente con un valor pequeño, tal que obligue a un primer paso*/
    radio_inicial = 0.01;
    double x0 = 0;
    double y0 = 0;
    char archivo[] = "Canal_ionico1.txt";
    datos = fopen (archivo, "r");
    while(!feof(datos)){
      
      fscanf(datos, "%f %lf\n%f %lf\n",&x1,&y1,&x2,&y2);
      radio = calcularRadio(x1,y1,x2,y2,radio_molecula);
      alpha = radio/radio_inicial;
      if(alpha > 1){
          radioMax = radio;
          centroX = x1;
          centroY = y1;
      }else{
          radioMax = radio_inicial;
          centroX = x0;
          centroY = y0;
      }
      x0 = x1;
      y0 = y1;
      radio_inicial = radio;
    }    
    /*Exportar resultados al archivo "Resultados.txt"*/
    resultados = fopen("Resultados.txt","w");
    fprintf(resultados, "%s\n", archivo);
    fprintf(resultados, "%lf\n", centroX);
    fprintf(resultados, "%lf\n", centroY);
    fprintf(resultados, "%lf\n", radioMax);
    fclose(resultados);
    return 0;    
}
/*Funcion que calculo la distancia entre dos puntos*/
double calcularRadio(double x1, double x2, double y1, double y2, double radio_molecula){
    double radio2;
    radio2 = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
    return pow(radio2, 0.5) - radio_molecula;
}