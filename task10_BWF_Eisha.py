import numpy as np
# Create a 1-dimensional array of integers
arr1 = np.array([1, 2, 3, 4, 5])
print("Array 1:", arr1)

# Create a 1-dimensional array of floats
arr2 = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
print("Array 2:", arr2)

# Get the shape of the arrays
print("Shape of Array 1:", arr1.shape)
print("Shape of Array 2:", arr2.shape)

# Get the data type of the arrays
print("Data type of Array 1:", arr1.dtype)
print("Data type of Array 2:", arr2.dtype)

# Create two multi-dimensional arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Add the two arrays
sum_arr = arr1 + arr2
print("Sum of arrays:\n", sum_arr)

# Subtract the two arrays
diff_arr = arr1 - arr2
print("Difference of arrays:\n", diff_arr)

# Multiply the two arrays
mult_arr = arr1 * arr2
print("Product of arrays:\n", mult_arr)

# Divide the two arrays
div_arr = arr1 / arr2
print("Division of arrays:\n", div_arr)