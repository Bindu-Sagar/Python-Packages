                       #NUMPY RANDOM
# Numpy has a random module to work with random numbers

# First we need to import random module from Numpy library
import numpy as np
from numpy import random as rd


# 1 Generating random values
# 1.1 Random integer
x=rd.randint(150)
print(x)
# Output :- The above statements gives the random variable from 0 to number given in parameter and the output varies every time

# 1.2 Random float(rand method)
x=rd.rand()
print(x)
# Output :- The above statement return random float values between 0 to 1

# 1.3 Random array(size as parameter)
# 1.3.1 Random integer array
arr=rd.randint(100,size=7)
print(arr)
# Output :- The above statement gives the an array of random number with array size 7 and each number is between 0 to 100

# 1.3.2 Random float array (pass a value to the rand which is the size of the array)
arr=rd.rand(4)
print(arr)
# Output :- The above statements gives the output as a array of random float values with size 4

# 1.3.3 Random 2-D array for both integers and float
arr1=rd.randint(100,size=(2,3))
arr2=rd.rand(2,3)
print(arr1)
print(arr2)
# Output :- Gives the Output of 2-D arrays with mentioned size.

# 1.3.4 Random values from the given array(choice function is used)
arr=[11,22,33,44,55,66]
x=rd.choice(arr)
print(x)
# Output :-  Gives a random value from the above mentioned array.

# Note you can also use size parameter to get a multi-dimensional array from the given array
arr1=rd.choice(arr,size=(3,5))
print(arr1)
# Output :-  Gives  random valued array as output with the above mentioned size from the given array

# 2.0 Random Permutations of the elements.
# 2.1 Shuffuling arrays
# 2.1.1 We have a function in numpy which is shuffle which is used to arrange the elements of a array in a randomdom order in itself
arr=np.array([1,2,3,4,5,6,7,8])
rd.shuffle(arr)
print(arr)
# The output is the converted array which is the shuffle of the original array.

# 2.1.2shuffle method changes the original array so to create another array  we use permutations method
arr2=rd.permutation(arr)
print(arr2)
# Output :- Here the array is an shuffled array while the original array remains same

# 3.0 SeaBorn Module
# Visualize Distributions With Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
# Before using the seaborn module which is in matplotlib install the seaborn using pip install seaborn command in terminal.
# Import the pyplot object of the Matplotlib module in your code using the following statement:
import matplotlib.pyplot as plt
# Now import the seaborn module
import seaborn as sns 
# Plotting a displot 
arr=np.array([0,1,2,4,5,7,8])
# sns.displot(arr)
# plt.show() # Uncomment to check the statement
# Ploting a displot wihout histogram
sns.displot([1,2,3,4,5,6], hist=False)
plt.show()
