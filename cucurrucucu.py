# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("Saminamina ee wakaka e e ")

x = [1,2,3]
y = [3,2,1]
f = plt.figure()
plt.plot(x,x)
plt.plot(y,y)
f.savefig("b.png")
