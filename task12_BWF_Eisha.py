import numpy as np

# Create a 2-dimensional array
arr = np.array([[1, 2], [3, 4]])

# Broadcast a scalar to the array
scalar = 5
result = arr + scalar

print(result)

# Create a 2-dimensional array
arr1 = np.array([[8, 2], [3, 4]])

# Create a 1-dimensional array
arr2 = np.array([10, 20])

# Broadcast arr2 to arr1
result1 = arr1 + arr2[:, np.newaxis]

print(result1)

# Create a 3-dimensional array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Create a 2-dimensional array
arr4 = np.array([[10, 20], [30, 40]])

# Broadcast arr2 to arr1
result2 = arr3 + arr4

print(result2)