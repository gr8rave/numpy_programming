'''
Created in Python 2.7.6 
Author - Bhavesh Bhatt
Date - 02nd June 2017
'''

import numpy as np
import matplotlib.pyplot as plt

radius = [1.0, 2.0, 3.0, 4.0]
area = [3.14159, 12.56636, 28.27431, 50.26544]
plt.xlabel('Radius')
plt.ylabel('Area')
plt.title('Area vs Radius Graph')
plt.axis([0,7,0,70])
plt.grid(True)
plt.text(2,30,'Hello')
plt.plot(radius, area)
plt.show()
