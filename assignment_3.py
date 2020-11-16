import numpy as np

#1 Create a numpy array starting from 2 till 50 with a stepsize of 3.

arr=np.arange(2,50,3)
print(arr)

#2 Accept two lists of 5 elements each from the user. Convert them to numpy arrays. Concatenate these arrays and print it. Also sort these arrays and print it.
ip1=np.array([int(input()) for i in range(5)])
ip2=np.array([int(input()) for i in range(5)])
print(np.sort(np.concatenate((ip1,ip2))))

#3 Write a code snippet to find the dimensions of a ndarray and its size.

arr=np.array([1,2,3,4,5,6])
print(arr.ndim)
print(arr.size)


#4 How to convert a 1D array into a 2D array? Demonstrate with the help of a code snippet
a = np.array([1, 2, 3, 4])
print(a)
b= np.reshape(a,(-1,2))
print(b)

#5 Consider two square numpy arrays. Stack them vertically and horizontally.
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.vstack(a))
print(np.hstack(a))

#6 How to get unique items and counts of unique items?
a=np.arange(1,10)
print(np.unique(a,return_counts=True))
