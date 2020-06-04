import numpy as np
import matplotlib.pyplot as plt

def calcula_coeficientes(w, wc, n):
    # determina os valores dos coeficientes segundo as expressões padronizadas
    Tn = np.zeros((w.size,))
    Tn[abs(w) < wc] = np.cos(n * np.arccos(w[abs(w) < wc] / wc))
    Tn[abs(w) >= wc] = np.cosh(n * np.arccosh(w[abs(w) >= wc] / wc))
    return Tn

def mod_Chebyshev(w,wc,n,e):
    #Calcula o modulo do filtro de Chebyshev
    modulo = 1 / ((1 + (e ** 2) * calcula_coeficientes(w, wc, n)**2) ** 0.5)
    return modulo

def mod_Butterworth(w,wc,n):
    #Calcula o módulo do filtro de Butterworth
    modulo = 1 / (1 + (w/wc)**(2*n))**0.5
    return modulo

def filtro(w,y):
    #Realiza a filtragem do sinal
    saida = []
    for k in range(100):
        saida.append(w[k] * y[k])
    return(saida)

w = np.linspace(0,20,100)
modulo_lista = []
cores = ['r','g','b','y','purple']

#Grafico1
for k in range (1,6):
    aux = mod_Chebyshev(w,5,k,0.2)
    modulo_lista.append(aux)
    plt.title("Módulo do filtro de Chebyshev")
    plt.plot(w,aux,color=cores[k-1])
plt.legend(("n = 1","n = 2","n = 3","n = 4","n = 5"))
plt.show()

#Grafico2
e_list = [0.1, 0.3, 0.5, 0.7, 0.9]
for k in range (5):
    aux = mod_Chebyshev(w,5,3,e_list[k])
    plt.title("Módulo do filtro de Chebyshev")
    plt.plot(w,aux,color=cores[k])
plt.legend(("e = 0.1","e = 0.3","e = 0.5","e = 0.7","e = 0.9"))
plt.show()

#Grafico3
for k in range(1,6):
    aux = mod_Butterworth(w,5,k)
    plt.title("Módulo do filtro de Butterworth")
    plt.plot(w,aux,color=cores[k-1])
plt.legend(("n = 1","n = 2","n = 3","n = 4","n = 5"))
plt.show()

#Grafico4
wc = 5
tau = 2*np.pi/wc
y = abs(2*np.sin(w*tau/2)/w)
plt.title("Módulo da Transformada de Fourier")
plt.plot(w,y)
plt.show()

#Graf5
filtro_ideal = []
for k in range(100):
    if (w[k]<5):
        filtro_ideal.append(1)
    else:
        filtro_ideal.append(0)

plt.title("Saída com filtro ideal")
plt.plot(w,filtro(filtro_ideal,y))
plt.show()

plt.title("Módulo do filtro ideal")
plt.plot(w,filtro_ideal)
plt.show()

#graf6
plt.title("Saída com filtro de Chebyshev")
plt.plot(w,filtro(mod_Chebyshev(e=0.9,n=3,wc=5,w=w),y))
plt.show()

plt.title("Módulo do filtro de Chebyshev")
plt.plot(w,mod_Chebyshev(e=0.9,n=3,wc=5,w=w))
plt.show()

#graf7
plt.title("Saída com filtro de Butterworth")
plt.plot(w,filtro(mod_Butterworth(n=2,wc=5,w=w),y))
plt.show()

plt.title("Módulo do filtro de Butterworth")
plt.plot(w,mod_Butterworth(n=2,wc=5,w=w))
plt.show()

#Graf8
plt.title("Comparação do Módulo dos filtros")
plt.plot(w,mod_Butterworth(n=2,wc=5,w=w), color="b")
plt.plot(w,mod_Chebyshev(e=0.9,n=3,wc=5,w=w), color="r")
plt.plot(w,filtro_ideal, color="g")
plt.legend(("Butterworth","Chebyshev","Ideal"))
plt.show()

plt.title("Saída após filtragem")
plt.plot(w,filtro(mod_Butterworth(n=2,wc=5,w=w),y), color="b")
plt.plot(w,filtro(mod_Chebyshev(e=0.9,n=3,wc=5,w=w),y), color="r")
plt.plot(w,filtro(filtro_ideal,y), color="g")
plt.legend(("Butterworth","Chebyshev","Ideal"))
plt.show()
