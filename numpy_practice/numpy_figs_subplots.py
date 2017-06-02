'''
Created in Python 2.7.6 
Author - Bhavesh Bhatt
Date - 02nd June 2017
'''

import numpy as np
import matplotlib.pyplot as plt

radius = [1.0, 2.0, 3.0, 4.0]
area = [3.14159, 12.56636, 28.27431, 50.26544]
t = np.arange(0., 5., 0.2)

plt.figure(1) 
    
plt.subplot(2,1,1)   
plt.plot(radius,area)


plt.subplot(2,1,2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**2, 'bs', t, t**3, 'g^')    

plt.show()

