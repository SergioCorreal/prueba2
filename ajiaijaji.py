# Ejercicio5
# imprima el mensaje: "hola mundo!" 
from scipy.fftpack import fft, fftfreq
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("Bebe yo te bote")

x = [1,2,3]
y = [3,2,1]
f = plt.figure()
plt.plot(x,x)
plt.plot(y,y)
f.savefig("b.png")
