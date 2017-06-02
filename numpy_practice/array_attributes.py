import numpy as np

a = np.arange(24).reshape(4,3,2)
print (a)

print ("Dimensions of A - ")
print (a.ndim)

print ("Shape of A - ")
print (a.shape)

print ("Number of elements in A - ")
print (a.size)

print ("dtype of A - ")
print (a.dtype)

print ("Size of elements of A - ")
print (a.itemsize)

print ("type of A - ")
print (type(a))
