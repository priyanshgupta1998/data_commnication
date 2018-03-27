import matplotlib.pylab as plt
import numpy as num

F1=int(input('Enter the frequency of carrier='))
F2=int(input('Enter the frequency of pulse='))

A=3;#Amplitude
t=num.arange(0,1,0.001)
x=A*num.sin(2*num.pi*F1*t)#Carrier Sine wave
u=[]#Message signal
b=[0.2,0.4,0.6,0.8,1.0]
s=1
for i in t:
    if(i==b[0]):
        b.pop(0)
        if(s==0):
            s=1
        else:
            s=0
        #print(s,i,b)
    u.append(s)
v=[]#Sine wave multiplied with square wave
for i in range(len(t)):
    v.append(A*num.sin(2*num.pi*F1*t[i])*u[i])
    


plt.subplot(3, 1, 1)
plt.title('ASK Generation')
plt.plot(x)
plt.ylabel('Amplitude')
plt.xlabel('message')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(u)
plt.ylabel('Amplitude')
plt.xlabel('carrier')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(v)
plt.ylabel('Amplitude')
plt.xlabel('Output signal')
plt.grid(True)
plt.show()


