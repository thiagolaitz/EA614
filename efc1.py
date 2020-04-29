import numpy as np
import matplotlib.pyplot as plt

h = np.array([1, -0.5],dtype=float)#resposta ao impulso
w1 = np.array([1,0.5, 0.5**2, 0.5**3, 0.5**4],dtype=float)#equalizador 1
w2 = np.array([1, 1.5, 0.7, -0.2, 0.3])#equalizador 2

def conv(a,b):
#Dados os vetores A e B calcula a convolução entre eles
    #encontrando a matriz de convolução e o vetor S
    h_len = len(a) + len(b) - 1

    h = np.zeros((h_len,h_len),dtype=float)#Matriz de convolução
    s = np.zeros((h_len,1),dtype=float)#vetor de entrada

    for i in range(h_len):#cria o vetor s
        if(i < len(b)):
            s[i] = b[i]

    #Cria a matriz H
    for j in range(h_len):#troca as colunas
        contador = 0

        if((j+len(a)) < h_len):
            indice = j + len(a)
        else:
            indice = h_len

        for i in range(j,indice):#troca as linhas
            h[i][j] = a[contador]
            contador += 1

    #Calcula a convolução
    y = np.dot(h,s)
    y = np.transpose(y)
    return y[0]

print("\nh*w1:\n",conv(h,w1))#Convolução h*w1
print("\nh*w2:\n",conv(h,w2))#Convolução h*w2

#Simulando a transmissão do sinal pelo canal

s = np.sign(np.random.randn(100))
x = conv(s,h)

print("\ns:\n",s)

print("\ns*h:\n",x)#calcula a convolução de s e h

#Filtrando os sinais

y1 = conv(x,w1)
y2 = conv(x,w2)

print("\ny1:\n",y1)
print("\ny2:\n",y2)

#Plotando os gráficos
x_graf1 = np.linspace(0,99,100)
x_graf2 = np.linspace(0,104,105)

plt.title("Análise entre s[n] e y1[n]")
plt.xlabel("n")
plt.ylabel("s[n] e y1[n]")
plt.stem(x_graf1, s, "b", markerfmt="bo", basefmt="gray", label="s[n]", use_line_collection = True)
plt.stem(x_graf2,y1, "r", markerfmt="ro", basefmt="gray", label="y1[n]", use_line_collection = True)
plt.legend()
plt.show()

plt.title("Análise entre s[n] e y2[n]")
plt.xlabel("n")
plt.ylabel("s[n] e y2[n]")
plt.stem(x_graf1, s, "b", markerfmt="bo", basefmt="gray", label="s[n]", use_line_collection = True)
plt.stem(x_graf2,y2, "r", markerfmt="ro", basefmt="gray", label="y2[n]", use_line_collection = True)
plt.legend()
plt.show()
