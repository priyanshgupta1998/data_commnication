#amlitude modulated waveform
import numpy as np
import matplotlib.pyplot as plt
# Carrier signal (Sc) = Ac*sin(2πfct)
# Message signal (Sm) = Am*sin(2πfmt)
# Modulated signal = (1+ m*sin(2*π*fm*t))*Ac*sin(2*π*fc*t)
#m=Am/Ac

Ac=1
fc=int(input('enter carrier frequency'))
fm=int(input('enter message frequency'))# fm<fc
m=float(input('enter modulation_index'))

Am=m*Ac

t1=np.arange(0,1,0.002)
message=np.sin(2*np.pi*fm*t1) # message signal
carrier=np.sin(2*np.pi*fc*t1) # carrier signal
output=(1+m*message)*(Ac*carrier)



plt.subplot(3, 1, 1)
plt.title('amplitude Modulation')
plt.plot(message)
plt.ylabel('Frequency')
plt.xlabel('Modulator signal')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(carrier)
plt.ylabel('Frequency')
plt.xlabel('Carrier signal')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(output)
plt.ylabel('Frequency')
plt.xlabel('Output signal')
plt.grid(True)
plt.show()









