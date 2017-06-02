'''
Created in Python 2.7.6 
Author - Bhavesh Bhatt
Date - 02nd June 2017
'''
import numpy as np
print ("Numpy version")
print (np.__version__+"\n")

python_list1 = [-5,-4,2,1]
my_array_from_list = np.array(python_list1)
print ("Array from python List")
print (my_array_from_list)
print ("======================="'\n')

# Print 1 dimensional array
one_d_array = np.array([1,2,3])
print ("one_d_array")
print (one_d_array)
print ("======================="'\n')

# Print 2 dimensional array
two_d_array = np.array ([(1.5,2,3),(4.0,5,6)], dtype = float)
print ("2 D Array")
print (two_d_array)
print ("======================="'\n')

#Arithmetic Operation
print ("Arithmetic Operation Multiplying each number with 2") 
print (2*one_d_array)
print ("======================="'\n')

# arange function
print (np.arange(7)) # Output between 0,1,2....6
print (np.arange(0,3,0.5)) # Output will be 0,0.5...3
print (np.arange(0,45,step = 7)) #Output will be in the steps of 7 till 45
print ("======================="'\n')

# linspace 
print (np.linspace(1, 10, num=5))
print ("======================="'\n')

# Zeros
print (np.zeros((2,4)))
print ("======================="'\n')

# Ones
print (np.ones((4,2)))
print ("======================="'\n')

#Slicing the array
print ("Slicing the array")
original_array1 = np.arange(10,20,1)
print ("Original array is = ")
print(original_array1)
print ("1st element is = ")
print (original_array1[0])
print ("2nd last element is = ")
print (original_array1[-2])
print ("======================="'\n')

#Reshaping an array
print ("Reshaping an array")
original_array2 = np.arange(35)
print("Before reshaping")
print (original_array2)
original_array2.shape = (5,7)
print ("After reshaping")
print (original_array2)
print ("======================="'\n')
print ("Printing 2nd last row of 2-D array")
print (original_array2[-2])
print ("======================="'\n')
print ("Printing 3rd row 3rd element")
print (original_array2[2,2])
print (original_array2[2][2])
print ("======================="'\n')

#Indexing
print ("Checking if values are divisible by 7")
my_vector1 = np.array([-17,-4,0,2,21,37,105])
zero_mod_7_mask = (my_vector1 % 7) == 0
print (zero_mod_7_mask)
print ("Now I wish to print the values which are non zero"'\n')
print(my_vector1[zero_mod_7_mask])
print ("======================="'\n')
my_vector1 = my_vector1[my_vector1 % 7 == 0]
print(my_vector1)

#Array Properties
print ("======================="'\n')
print (original_array2)
print ("Printing dimensions of the array")
print(original_array2.shape)
print ("Printing the number of dimensions of the array")
print(original_array2.ndim)
print ("Printing the number of elements in the array")
print (original_array2.size)
print ("Printing the type of elements in the array")
print (original_array2.dtype)
print ("======================="'\n')

#Matrix Multiplication of the 2 arrays
left_mat = np.arange(6).reshape((2,3))
right_mat = np.arange(15).reshape((3,5))
print (np.dot(left_mat,right_mat))

#Broadcasting
mat1 = np.arange(70).reshape((2,7,5))
print ("Broadcasting Example")
print (mat1)
print ("Sum all the numbers in the array")
print (mat1.sum(axis=0))

#Creatring Structured Arrays & Record Arrays
person_data_def = [('name','S16'),('age','i8')]
people_array = np.zeros((2),dtype = person_data_def)
print ("Structured array format")
print (people_array)
'''
Structured array format
[('', 0) ('', 0)]
'''
people_array[0] = ('Bhavesh',25)
people_array[1] = ('Undertaker',51)
print (people_array)
'''
[('Bhavesh', 25) ('Undertaker', 51)]
'''
print(people_array[0]['age'])
'''
[25 51]
'''

person_record_array = np.rec.array([('Bhavesh',25),('Undertaker',51)],dtype = person_data_def)
print (person_record_array)
'''
[('Bhavesh', 25) ('Undertaker', 51)]
'''
print(person_record_array[0].age)


