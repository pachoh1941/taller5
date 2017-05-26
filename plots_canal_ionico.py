import numpy as np
import matplotlib.pyplot as plt
#Se importan los resultados del archivo en C
with open('Resultados.txt', 'r') as myfile:
    datos = myfile.readlines()
archivo = datos[0].rstrip()
centroX = float(datos[1])
centroY = float(datos[2])
radioMax = float(datos[3])
coordenadas = np.loadtxt(archivo)
coordenadasX = coordenadas[:,0]
coordenadasY = coordenadas[:,1]
#Grafica del circulo y los demas puntos
puntos = 1000
circulo = plt.Circle((centroX, centroY), radioMax, fill = False)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(coordenadasX, coordenadasY)
ax.add_artist(circulo)
ax.set_title('Parametros: x = '+str(centroX)+', y = '+str(centroY)+', radio = '+str(radioMax))
ax.set_xlabel('X'+r'$(\AA)$')
ax.set_ylabel('Y'+r'$(\AA)$')
plt.savefig('circulo.png')