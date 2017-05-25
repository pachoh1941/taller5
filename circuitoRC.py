import numpy as np
import matplotlib.pyplot as plt
#Carga de datos
datos = np.loadtxt('CircuitoRC.txt')
t_obs = datos[:,0]
y_obs = datos[:,1]
#Funciones para utilizar
def verosimilitud(y_obs, y_modelo):
    varianza = 1.0
    chi_cuadrado = (1.0/(2.0*varianza*varianza))*sum((y_obs-y_modelo)**2)
    return np.exp(-chi_cuadrado)
def modelo(t, R, C, Q_max):
    return Q_max*(1-np.exp(-t/(R*C)))
#Inicializacion 
R_walk = np.empty((0))
C_walk = np.empty((0))
Q_max_walk = np.empty((0))
l_walk = np.empty((0)) #Verosimilitud
desvesta = 0.005
#Inicializacion
#Se incializo tomando valores de R, C y Q_max tales que chi_cuadrado fuese lo mas pequeno posible, porque los valores de verosimilitud daban
#magnitudes que el programa aproximaba a cero, haciendo imposible el calculo de alpha.
R_inicial = np.random.normal(100.0, desvesta)
C_inicial = np.random.normal(0.609, desvesta)
Q_max_inicial = np.random.normal(100.0, desvesta)
R_walk = np.append(R_walk, R_inicial)
C_walk = np.append(C_walk, C_inicial)
Q_max_walk = np.append(Q_max_walk, Q_max_inicial)
#Primer lanzamiento
y_inicial = modelo(t_obs, R_walk[0],C_walk[0],Q_max_walk[0])
l_walk = np.append(l_walk, verosimilitud(y_obs,y_inicial))
#Caminata
iteraciones = 20000
for i in range(iteraciones):
    #Siguiente paso
    R_prima = np.random.normal(R_walk[i],desvesta)
    C_prima= np.random.normal(C_walk[i],desvesta)
    Q_max_prima = np.random.normal(Q_max_walk[i],desvesta)
    #MCMC
    y_inicial = modelo(t_obs, R_walk[i],C_walk[i],Q_max_walk[i])
    y_prima = modelo(t_obs, R_prima,C_prima,Q_max_prima)
    
    l_prima = verosimilitud(y_obs, y_prima)
    l_inicial = verosimilitud(y_obs, y_inicial)
    alpha = l_prima/l_inicial
    if(alpha>=1.0):
        R_walk = np.append(R_walk,R_prima)
        C_walk = np.append(C_walk,C_prima)
        Q_max_walk = np.append(Q_max_walk, Q_max_prima)
        l_walk = np.append(l_walk, l_prima)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            R_walk = np.append(R_walk,R_prima)
            C_walk = np.append(C_walk,C_prima)
            Q_max_walk = np.append(Q_max_walk, Q_max_prima)
            l_walk = np.append(l_walk, l_prima)
        else:
            R_walk = np.append(R_walk, R_walk[i])
            C_walk = np.append(C_walk, C_walk[i])
            Q_max_walk = np.append(Q_max_walk, Q_max_walk[i])
            l_walk = np.append(l_walk, l_inicial)
#Obtencion de los parametros de maxima verosimilitud
max_verosimilitud = np.argmax(l_walk)
R = R_walk[max_verosimilitud]
C = C_walk[max_verosimilitud]
Q_max = Q_max_walk[max_verosimilitud]
#Graficas
#Histograma R
count, bins, ignored = plt.hist(R_walk, 20, normed = True)
plt.title('Histograma del parametro R')
plt.savefig('histR.png',bbox_inches='tight')
plt.close()
#Rvsl
plt.scatter(R_walk, -np.log(l_walk))
plt.xlabel('Estimacion de R')
plt.ylabel('Verosimilitud (base ln)')
plt.savefig('graf_RvLike.png',bbox_inches='tight')
plt.close()
#Histograma C
count, bins, ignored = plt.hist(C_walk, 20, normed = True)
plt.title('Histograma del parametro C')
plt.savefig('histC.png',bbox_inches='tight')
plt.close()
#Cvsl
plt.scatter(C_walk, -np.log(l_walk))
plt.xlabel('Estimacion de C')
plt.ylabel('Verosimilitud (base ln)')
plt.savefig('graf_CvLike.png',bbox_inches='tight')
plt.close()
#DatosvsModelo
y_fit = modelo(t_obs, R, C, Q_max)
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.plot(t_obs, y_fit, 'r', linewidth = 3.0)
ax3.scatter(t_obs, y_obs)
ax3.set_xlabel('Tiempo (s)')
ax3.set_ylabel('Carga (A)')
ax3.set_title('Datos reales y curva de ajuste con parametros:\nR = '+str(R)+'\nC = ' + str(C))
fig3.savefig('graf_modelo.png', bbox_inches='tight')
plt.close(fig3)