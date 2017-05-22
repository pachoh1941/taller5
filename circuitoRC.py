import numpy as np
import matplotlib.pyplot as plt
#Carga de datos
datos = np.loadtxt('CircuitoRC.txt')
t_obs = datos[:,0]
y_obs = datos[:,1]
plt.scatter(t_obs, y_obs)
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

R_walk = np.append(R_walk, 100)
C_walk = np.append(C_walk, 0.609)
Q_max_walk = np.append(Q_max_walk, 100.0)
#Primer lanzamiento
y_inicial = modelo(t_obs, R_walk[0],C_walk[0],Q_max_walk[0])
l_walk = np.append(l_walk, verosimilitud(y_obs,y_inicial))
#Primer lanzamiento
y_inicial = modelo(t_obs, R_walk[0],C_walk[0],Q_max_walk[0])
l_walk = np.append(l_walk, verosimilitud(y_obs,y_inicial))
#Caminata
iteraciones = 20000
desvesta = 0.1
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
#Graficas
max_verosimilitud = np.amax(l_walk)
R = R_walk[np.where(l_walk == max_verosimilitud)]
C = C_walk[np.where(l_walk == max_verosimilitud)]
Q_max = Q_max_walk[np.where(l_walk == max_verosimilitud)]