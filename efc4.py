import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sio
import sounddevice as sd
from scipy import signal

Fs, y = sio.read('queen_I_want_it_all.wav')
z = y
y = y[:,0]+y[:,1]

def espectro(y):
    """ Rotina que exibe o espectro de magnitude (X(ejw)) de um sinal discreto """
    # modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    # frequencias avaliadas
    w = np.linspace(0, 2 * math.pi, Y.size)

    # exibe o grafico do espectro
    plt.figure()
    plt.plot(w, Y / np.max(Y))
    plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)
    plt.grid(True)
    plt.xlim((0, 2 * math.pi))
    plt.show()

    return Y

def kaiser(wp, wr):
    wc = (wp + wr) / 2
    d = 0.01
    Ap = 20 * math.log10((1 + d) / (1 - d))
    Ar = -20 * math.log10(d)

    if Ar < 21:
        b = 0
        D = .9222

    elif Ar < 50:
        b = 0.5842 * (Ar - 21) ** 0.4 + 0.07886 * (Ar - 21)
        D = (Ar - 7.95) / 14.36
    else:
        b = .1102 * (Ar - 8.7)
        D = (Ar - 7.95) / 14.36

    k = math.ceil(math.pi * D / (wr - wp) - .5)
    M = 2 * k + 1

    n = np.arange(-k, k + 1, 1)

    w = np.i0(b * np.sqrt(1 - (4 / M ** 2) * n ** 2))
    w = np.divide(w, np.i0(b))

    h = wc / math.pi * np.sinc(wc * n / math.pi) * w

    return h

def decimacao(M,y):
    y_dec = []
    for k in range(len(y)):
        if (k%M == 0):
            y_dec.append(y[k])
    return y_dec

espectro(y)
espectro(decimacao(6,y))

sd.play(y,44100)
status = sd.wait()
sd.play(decimacao(6,y),44100/6)
status = sd.wait()

#Análise em freq da resposta ao impulso dos filtros
espectro(kaiser(0.45,2))
espectro(kaiser(0.45,0.5))
espectro(kaiser(1.5,2))

#Análise do áudio com filtro anti-aliasing
y_filtrado = signal.convolve(y, kaiser(0.45,0.5))
espectro(y_filtrado)
sd.play(y_filtrado,44100)
status = sd.wait()

#Análise do áudio subamostrado filtrado
y_sub_filtrado = signal.convolve(y, kaiser(0.45,0.5))
y_sub_filtrado = decimacao(6,y_sub_filtrado)
espectro(y_sub_filtrado)
sd.play(y_sub_filtrado,44100/6)
status = sd.wait()
