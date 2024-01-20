print('ds and')
# To use the numpy commands import the numpy package as below 
import numpy  
# You can also use another name to the import as "import numpy as np"

# To view the version of the numpy use the below command
print(numpy.__version__)

                        # CREATING ARRAY

# To create a numpy array use the numpy command as below
# 1
arr1=numpy.array([1,2,3])
print(arr1)
# Output
# [1,2,3]

# 2 Use list or tuple or other type to the array command to make them to a ndarray
list1=[1,2,3,4,5]
tuple1=(1,2,3,4,5,6,7)
arr2=numpy.array(list1)
arr3=numpy.array(tuple1)
print(arr2,arr3)

# Use the default command type(array_name) to view the type of the array (to look how the array type is stored)
print(type(arr1))

# Using the N-dimensional arrays using the N-dimensional ndarrays
# 0-dimension
arr1=numpy.array(45)

# 1-dimension
arr2=numpy.array([1,2,3,4])

# 2-dimension
arr3=numpy.array([[1,2,3,4],[5,6,7,8]])

# 3-dimension
arr4=numpy.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

# To viem the number of dimension we have use array.ndim command 
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.

arr4=numpy.array([1,2,3,4],ndmin=5)
print(arr4,arr4.ndim)


                    # ARRAY INDEXING

# Array indexing is the same as accessing an array element.
# You can access an array element by referring to its index number.
# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
print(arr2[2], arr3[0][1])

# Access 2-D Arrays
# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
# Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

print('1-row 2-column: ',arr3[0,1])

# Access 3-D Arrays
# Same as 2-D with additonal parameter
arr4=numpy.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(arr4[0,1,2])

# Negative Indexing
# Use negative indexing to access an array from the end.
print(arr4[-1,-1,-3])

                        # ARRAY SLICING

# #Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

arr=numpy.array([1,2,3,4,5,6,7,8])
print(arr[3:5])
print(arr[4:])
print(arr[:4])
print(arr[1:5:2])

# Negitive Slicing
# Use -ve sign for the indices

print(arr[-4:-1])
print(arr[-3:])
print(arr[:-5])  
print(arr[-1:-5:-1])

# Slicing 2-D arrays 

arr=numpy.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1,1:3])

# From both elements, return index 2
print(arr[0:2,2])

# From both elements, slice index 1 to index 3 (not included), this will return a 2-D array
print(arr[0:3,1:3])


                        # NUMPY DATA TYPES

# Python has some default data types such as integer,sting float,boolean and complex.
# Numpy has some extra dayta types which can be indicated by just one characters such as i,f etc.,
# Below are the differnent data type use d in the numpy
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# The command dtype is used to view the type of data we have in numpy

arr=numpy.array([1,2,3,4,5])
arr1=numpy.array(["sagar","revanth","naveen"])
print(arr.dtype,arr1.dtype)

# use the dtype command  as the parameter while initilizing the numpy array to 
# get the array in the desiginated array type
arr=numpy.array([1,2,3,4,5], dtype='S')
print(arr,arr.dtype)

# For i, u, f, S and U we can define size as well
# Example for integer with 4 bytes data size.
arr=numpy.array([1,2,3,4,5],dtype='i4')
print(arr.dtype)

# Numpy will raise the value error if the value can not be casted to a designated data type.
# Uncomment the below line to see the error
# arr=numpy.array([1,2,3,4,'a'], dtype='i')

# Numpy also have a command as astype which is used to duplicate an array with differnt data type
arr=numpy.array([1.1,2.3,3.5])
arr2=arr.astype('i')
print(arr2,arr2.dtype,arr.dtype)


arr3=arr.astype(int)
arr4=arr.astype(bool)

print(arr3.dtype,arr4.dtype)


# About Copy and View 
# Copy owns the data
# Copy command is used to duplicate the array and the modifications to the array doesn't affect the original array
arr=numpy.array([1,2,3,4,5])
x=arr.copy()
arr[0]=7
print(x,arr)

# View command works as same copy except it affectrs the original array
# View doesn't owns the data
y=arr.view()
arr[0]=45
print(arr,y)

# If you change the values of the view it affects the original array
y[1]=10
print(arr,y)

# In numpy there is command known as base that return NONE if array owns the data
print(x.base,y.base)

# SHAPE command returns the number of elements in each dimension
arr=numpy.array([[1,2,3,4],[1,2,3,4]])
print(arr.shape) # This return as (2,4) which mean it is 2-D with 4 elemnts in each array

arr=numpy.array([1,2,3],ndmin=5)
print(arr.shape)

# Reshape is used to change the shape of the array
arr=numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])
x=arr.reshape(4,3)

print(x) 

# Its gives the output of array x as
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

y=arr.reshape(2,3,2)
z=arr.reshape(2,2,3)
print(y) # It gives a 3 dimension array as output

# Output of y
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]

# The array which is return from reshape is a view
print(z.base) 
# The output is 
# [1,2,3,4,5,6,7,8,9,10,11,12]     so it is the original array

# Unknown dimension is used if you do not have specific number for any one of the dimension in the reshape method
# Pass -1 value and numpy automatically calculate its value
x=arr.reshape(2,2,-1)
print(x)
# the Output is 
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]]
# Note: We can not pass -1 to more than one dimension.

# Flattening an array mean converting an array into a 1-D array
# Use reshape(-1) to convert the array into a 1-D array
x=x.reshape(-1)
print(x)
# the output is 
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

# Iterating the array
# 1-D arrays 
arr=numpy.array([1,2,3,4,5,6,7,8,9,0])
for i in arr:
    print(i)

# 2-D array
x=arr.reshape(2,-1)
for i in x:
    print(i)

# Iterate on each scalar element
for i in x:
    for j in i: 
        print(j)

print("hello world")