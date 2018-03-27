#frequency modulated waveform
import numpy as np
import matplotlib.pyplot as plt

mf = 4.0#Hz
cf = 60.0#Hz
mindex = 1.0

time = np.arange(44100.0) / 44100.0

modulator = np.sin(2.0 * np.pi * mf * time) * mindex #sinusoidal signal

carrier = np.sin(2.0 * np.pi * cf * time)#carrier signal;

product = np.zeros_like(modulator)

for i, t in enumerate(time):
    product[i] = np.sin(2. * np.pi * (cf* t + modulator[i]))

plt.subplot(3, 1, 1)
plt.title('Frequency Modulation')


plt.plot(modulator)
plt.ylabel('Amplitude')
plt.xlabel('Modulator signal')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(carrier)
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(product)
plt.ylabel('Amplitude')
plt.xlabel('Output signal')
plt.grid(True)

plt.show()












