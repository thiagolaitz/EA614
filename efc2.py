import numpy as np
import matplotlib.pyplot as plt

def fourier(t,n,rep=2000,filtro=None):
#Calcula o vetor y e x para a o plot da série de Fourier - dente de serra
#Calcula a energia do erro
#Salva os coeficientes Ak
    global x,y,energia_erro,coeficiente_vetor,vetor_w

    if filtro is None:
        filtro = []
        for j in range(2*n+1):
            filtro.append(1)

    x = np.linspace(-t,t,rep)
    y = []  #armazena os valores da série de Fourier

    energia_erro = 0

    for g in range(rep):
        soma = complex(0,0)
        coeficiente_vetor = []
        vetor_w = []
        contador = 0#contador para o indice do filtro

        for k in range(-n,n+1):
            if(k != 0):

                coeficiente = filtro[contador]*complex(0,((-1)**(k))/(k*np.pi))
                soma += coeficiente * (np.exp(complex(0,k*x[g]*np.pi/2)))
                coeficiente_vetor.append(abs(coeficiente))
                contador += 1
            else:
                contador +=1
                coeficiente_vetor.append(0)

            vetor_w.append(k*np.pi/2)#Cria o vetor w:

        y.append(soma)
        energia_erro += (soma - x[g]/2)**2
    energia_erro = energia_erro/(2*t)
    filtro = []

vetor_n = [1,10,20,50]#Possíveis valores de N
vetor_energia = []#Salva a energia do erro

for k in range(4):
    fourier(2,vetor_n[k])
    plt.title("Dente de Serra e Aproximação por Fourier: N = {}".format(vetor_n[k]))
    plt.plot(x, y, "b", label="Fourier")
    plt.plot(x,x/2, "r", label="Dente de serra")
    plt.legend()
    plt.xlabel("t[s]")
    plt.ylabel("x(t)")
    plt.show()
    vetor_energia.append(float(energia_erro))

#Plot dos coeficientes para N = 50
fourier(2,50)
plt.title("Plot dos coeficientes em função de Kw0")
plt.xlabel("k*w0")
plt.ylabel("Ck")
plt.stem(vetor_w,coeficiente_vetor, use_line_collection=True)
plt.show()

#Calculando a resposta em frequência de um filtro RC
wc = 1/(100000*10**(-6))
h_abs = []#Vetor da resposta em freq -- módulo
h_fase = []#Vetor da resposta em freq -- fase
H = []#Vetor da resposta em freq -- complexo

for k in range(len(vetor_w)):
    if(vetor_w[k] != 0):
        valor = 1/(1-complex(0,wc/vetor_w[k]))
        h_abs.append(abs(valor))
        h_fase.append(np.angle(valor))
        H.append(valor)
    else:
        h_abs.append(0)
        h_fase.append(0)
        H.append(0)

print(H)

#Plotando módulo e fase de H:
plt.title("Módulo de H em função de w")
plt.xlabel("K*w0")
plt.ylabel("Abs(H)")
plt.stem(vetor_w, h_abs, use_line_collection=True)
plt.show()

plt.title("Fase de H em função de w")
plt.xlabel("K*w0")
plt.ylabel("Angle(H)")
plt.stem(vetor_w, h_fase, use_line_collection=True)
plt.show()

#Plotando a série de Fourier após o filtro:
fourier(2,50,10000,filtro=H)
plt.title("Série de Fourier após filtro")
plt.xlabel("t[s]")
plt.ylabel("x(t)")
plt.plot(x,y)
plt.show()
