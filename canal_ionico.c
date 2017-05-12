#include <stdio.h>
#include <stdlib.h>
/*Declaracion de funciones*/
int contarLineas(char filename, FILE *datos);
void cargarDatos(char filename, FILE *datos, double *arrayX, double *arrayY);
/*Main*/
int main()
{
    int num_lineas;
    int i;
    FILE *datos;
    /*Archivo con los datos a leer*/
    char archivo[] = "Canal_ionico.txt";
    /*----------------------------*/
    num_lineas = contarLineas(archivo, datos);
    double *coordenadasX;
    coordenadasX = malloc(num_lineas*sizeof(double));
    double *coordenadasY;
    coordenadasY = malloc(num_lineas*sizeof(double));
    cargarDatos(archivo, datos, coordenadasX, coordenadasY);
    for(i=0;i<num_lineas;i++){
        printf("%f %f\n", coordenadasX[i], coordenadasY[i]);
    }
    return 0;
}
/*Funcion para leer las lineas de un archivo*/
int contarLineas(char filename, FILE *datos)
{
    datos = fopen(filename, "r");
    int lineas = 0;
    while(!feof(datos))
    {
        ch = fgetc(datos);
        if(ch == '\n'){
            lineas++;
        }
    }
    fclose(datos);
    return lineas;
}
/*Funcion para leer los datos del archivo y guardarlos en arrays*/
void cargarDatos(char filename, FILE *datos, double *arrayX, double *arrayY)
{
    int i;
    double x,y;
    int lineas = contarLineas(filename, datos);
    datos = fopen (filename, "r");
    for(i=0;i<lineas;i++){
        fscanf(datos, "%f %f",&x,&y);
        arrayX[i] = x;
        arrayY[i] = y;
    }    
    fclose(datos);
}