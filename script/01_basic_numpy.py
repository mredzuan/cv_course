import numpy as np

mylist = [1,2,3]
type(mylist)


myArray = np.array(mylist)


np.arange(0,10,2)

np.zeros(shape=(10,5))

np.ones(shape=(2,4))


np.random.seed(101)
arr = np.random.randint(0,100,10)

arr2 = np.random.randint(0,100,10)

arr.max()
arr.argmax()

arr.min()
arr.argmin()
arr.mean()
arr.shape

arrReshape = arr.reshape(2,5)


mat = np.arange(0,100).reshape(10,10)
mat.shape

mat[4,6]

mat[:,1]
mat[:, 1].reshape(10,1)

mat[2, :]


myNeMat = mat.copy()

myNeMat[0:6, :] = 999



#Exercise
#1. Create a 5 by 5 array with every number is a 10

fbf_array = np.ones(shape=(5,5))*10

#2. Largest and smaller numbers

np.random.seed(101)

arr_rand = np.random.randint(low=0, high= 100, size=(5,5))

# smaller value
arr_rand.min()

# Larger value
arr_rand.max()




