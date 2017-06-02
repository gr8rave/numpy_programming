import numpy as np

a = np.arange(24)
print (a)
print ("\n")

# Adding new elements
a1 = np.append (a, np.arange(100,105,1))
print ("Appening values in A matrix")
print (a1)

# Inserting the value
a2 = np.array([[1, 1], [2, 2], [3, 3]])
print (a2)
a2 = np.insert(a2, 0, 10)
print (a2)

# Deleting the value
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print (arr)
print ('\n')
print ("Delete from 0 0 ")
print (np.delete(arr, 0,1 ))
print ('\n')

print ("Delete from 1 0 ")
print (np.delete(arr, 1, 0))
print ('\n')

print ("Delete from 2 0 ")
print (np.delete(arr, 2, 0))
print ('\n')

print ("Delete from 0 1 ")
print (np.delete(arr, 0, 1))
print ('\n')

print ("Delete from 1 1 ")
print (np.delete(arr, 1, 1))
print ('\n')

