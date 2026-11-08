#1.WAP for ndarray Object, Indexing, and Slicing.
Ans:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Element at (0, 1):", arr[0, 1]) # Indexing
print("Row 1:", arr[1, :]) # Slicing rows
print("Column 2:", arr[:, 2]) # Slicing columns

            #OUTPUT
Array:
 [[1 2 3]
 [4 5 6]]
Element at (0, 1): 20
Row 1: [40 50 60]
Column 2: [30 60]

#2.WAP for Data Types and Structures in NumPy.
Ans:
arr = np.array([1, 2, 3], dtype='int32')
print("Data type:", arr.dtype)
arr = arr.astype('float64')
print("Updated type:", arr.dtype)

                #OUTPUT
Data type: int32
Updated type: float64

#3.WAP for NumPy Array Properties and Functions.
Ans:
ones_array = np.ones((2, 3))
zeros_array = np.zeros((2,
3))
empty_array = np.empty((2,
3))
print("Ones:\n", ones_array)
print("Zeros:\n",
zeros_array)
print("Empty:\n",
empty_array)
arr = np.array([[1, 2, 3], [4,
5, 6]])
print("Shape of array:",
arr.shape)
reshaped = arr.reshape(3, 2)
print("Reshaped array:\n",
reshaped)
arr1 = np.array([1, 2, 3])
copy_arr1 = arr1.copy()
view_arr1 = arr1.view()
print("Original:", arr1)
print("Copy:", copy_arr1)
print("View:", view_arr1)
arr2 = np.array([1, 2])
arr3 = np.array([3, 4])
concatenated =
np.concatenate((arr2, arr3))
print("Concatenated array:",
concatenated)
arr4 = np.array([5, 2, 9, 1])
print("Sorted array:",
np.sort(arr4))


           #OUTPUT
Ones:
 [[1. 1. 1.]
 [1. 1. 1.]]
Zeros:
 [[0. 0. 0.]
 [0. 0. 0.]]
Empty:
 [[0. 0. 0.]
 [0. 0. 0.]]
Shape of array: (2, 3)
Reshaped array:
 [[1 2]
 [3 4]
 [5 6]]
Original: [1 2 3]
Copy: [1 2 3]
View: [1 2 3]
Concatenated array: [1 2 3 4]
Sorted array: [1 2 9 5]

#4.WAP for Statistical Operations and Broadcasting on Arrays.
Ans:
arr = np.array([1, 2, 3, 4])
print("Max:", arr.max())
print("Min:", arr.min())
print("Sum:", arr.sum())
print("Product:", arr.prod())
print("Broadcasted result:", arr + 5)

           #OUTPUT
Max: 4
Min: 1
Sum: 10
Product: 24
Broadcasted result: [6 7 8 9]

#5.WAP for Saving and Loading Arrays.
Ans:
arr = np.array([1, 2, 3, 4])
np.save('my_array', arr) # Save array
loaded_arr = np.load('my_array.npy') # Load array
print("Loaded array:", loaded_arr)

                   #OUTPUT
Loaded array: [1 2 3 4]
