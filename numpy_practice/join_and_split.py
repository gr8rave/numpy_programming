import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6]])
print (arr1)
print ('\n')
print (arr2)
print ('\n')
arr_concat_along_row = np.concatenate((arr1,arr2), axis = 0)
print (arr_concat_along_row)


