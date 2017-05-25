import numpy as np
import matplotlib.pyplot as plt
#Se importan los resultados del archivo en C
datos = np.loadtxt('Resultados.txt')
centroX = datos[0,:]
centroY = datos[1,:]
radioMax = datos[2,:]
coordenadasX = np.zeros(len(datos)-3)
coordenadasY = np.zeros(len(datos)-3)
for i in range(3,len(datos)-1):
    coordenadasX[i]=datos[i,0]   
    coordenadasY[i]=datos[i,1]
#Grafica del circulo y los demas puntos
puntos = 1000
limsX = [np.amin(coordenadasX), np.amax(coordenadasX)]
limsY = [np.amin(coordenadasY), np.amax(coordenadasY)]
x = np.linspace(limsX[0],limsX[1],puntos)
y = np.linspace(limsY[0],limsY[1],puntos)
dondeCirculoExiste = np.where((((x*x)-centroX)+((y*y)-centroY))==radioMax)
plt.plot(x[dondeCirculoExiste], y[dondeCirculoExiste])
plt.scatter(coordenadasX, coordenadasY)
plt.title('Parametros: x = '+str(centroX)+', y = '+str(centroY)+', radio = '+str(radioMax))
plt.xlabel = ('X'+r'$\AA$')
plt.ylabel = ('Y'+r'$\AA$')