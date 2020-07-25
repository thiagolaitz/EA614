import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sci

x = np.linspace(0,63,64)
y = []
f0 = 3 #Hz
fs = 64 #Hz
omega = np.linspace(0,6.28,64)

for n in range(64):
    y.append(np.sin(2*np.pi*n*f0/fs))

plt.stem(x,y)
plt.title("Sequência X[n]")
plt.xlabel("n")
plt.ylabel("X[n]")
plt.show()

#Cálculo de x(K) e X(e^jw)
xk = np.abs(np.fft.fft(y))
a,x_omega = sci.freqz(y,1,worN=5000)
x_omega = np.abs(x_omega)

#Gráfico para comparação de X(K) e X(e^jw)
plt.stem(omega,xk,'r',label="|x(K)|")
plt.plot(a,x_omega,label="|x($e^{j\Omega}$)|")
plt.xlabel("$\Omega$ [rad]")
plt.ylabel("|x($e^{j\Omega}$)|")
plt.title("Comparação entre |x(K)| e |x($e^{j\Omega}$)|")
plt.xlim(0,np.pi)
plt.legend()
plt.show()

#Cálculo de x(K) para 2N
xk = np.abs(np.fft.fft(y,128))
omega = np.linspace(0,6.28,128)

#Gráfico para comparação de X(K)(2N) e X(e^jw)
plt.stem(omega,xk,'r',label="|x(K)|")
plt.plot(a,x_omega,label="|x($e^{j\Omega}$)|")
plt.xlabel("$\Omega$ [rad]")
plt.ylabel("|x($e^{j\Omega}$)|")
plt.title("Comparação entre |x(K)|(2N) e |x($e^{j\Omega}$)|")
plt.xlim(0,np.pi)
plt.legend()
plt.show()

#Mudança para f0 = 3.4 Hz
f0 = 3.4 #Hz
y = []
for n in range(64):
    y.append(np.sin(2*np.pi*n*f0/fs))

#Nova sequência com f0 = 3.4 Hz
plt.stem(x,y)
plt.title("Sequência X[n], f0 = 3.4 Hz")
plt.xlabel("n")
plt.ylabel("X[n]")
plt.show()

#Cálculo de x(K) e X(e^jw)
xk = np.abs(np.fft.fft(y))
a,x_omega = sci.freqz(y,worN=5000)
x_omega = np.abs(x_omega)
omega = np.linspace(0,6.28,64)

plt.stem(omega,xk,'r', label="|x(K)|")
plt.plot(a,x_omega, label="|x($e^{j\Omega}$)|")
plt.xlabel("$\Omega$ [rad]")
plt.ylabel("|x($e^{j\Omega}$)|")
plt.title("Comparação entre |x(K)| e |x($e^{j\Omega}$)|, f0 = 3.4Hz")
plt.xlim(0,np.pi)
plt.legend()
plt.show()
