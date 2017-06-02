import numpy as np

# Copy 1 array from the other
# Elements of a1 and a2 are located in the same memory location
a1 = np.arange(10)
a2 = a1
print (a1)
print (a2 is a1)
a2 [7] = 45
print (a2)
print (a1)
#Memory locations of a1 and a2 are the same which we can verify from below
print (id(a1))
print (id(a2))

# Shallow copy
# Create 2 arrays
a3 = np.arange(10,20,1)
a4 = a3.view()
a4.shape = (2,5)
print (a3)
print (a4)
# Memory locations of a3 and a4 are also the same 
a3[5] = 67
print (a3)
print (a4)
print (id(a3))
print (id(a4))

#Deep Copy - we copy all elements from a3 to a5 and this is actual copy whereas the above 2 methods are mostly references to the actual copy.
a5 = np.copy(a3)
a5 [0] = -121
print (a3)
print (a5)
print (id(a3))
print (id(a5))

