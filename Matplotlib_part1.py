#Matplotlib part 1

#Import libraries
from re import X
import matplotlib.pyplot as plt
import numpy as np

#Create vectors
x = np.linspace(0,5,11)
print(x)
y = x*x 
print(y)

#Plot graphic with values
plt.plot(x,y,'r-*')
plt.show()

#Exploring methods
plt.plot(x,y,'y-*')
plt.xlabel('axis X')
plt.ylabel('axis y')
plt.title('Generic Title')
plt.show()

#Plot multiple graphics
plt.subplot(1,2,1)
plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.plot(y,x,'g*-')
plt.show()

#Define figure
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.25,0.25,0.50,0.50])
axes1.plot(x,y)
axes1.set_xlabel('Axis X')
axes1.set_title('Generic title 2')
axes2.plot(y,x)
plt.show()