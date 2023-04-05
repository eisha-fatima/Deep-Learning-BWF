import numpy as np
import matplotlib.pyplot as plt

# Create a 1-dimensional array of integers
arr = np.array([1, 2, 3, 4, 5])

# Mean of the array
mean = np.mean(arr)
print("Mean:", mean)

# Median of the array
median = np.median(arr)
print("Median:", median)

# Mode of the array
mode, count = np.unique(arr, return_counts=True)
mode_index = np.argmax(count)
mode_value = mode[mode_index]
print("Mode:", mode_value)


# 25th and 75th percentiles (i.e., Q1 and Q3)
q1, q3 = np.percentile(arr, [25, 75])
print("Q1:", q1)
print("Q3:", q3)

# Interquartile range (IQR)
iqr = q3 - q1
print("IQR:", iqr)

# Rank of the array elements
rank = np.argsort(arr)
print("Rank:", rank)

# Create a normal distribution with mean 0 and standard deviation 1
mu, sigma = 0, 1
dist = np.random.normal(mu, sigma, 1000)

# Plot the histogram of the distribution
count, bins, ignored = plt.hist(dist, 30, density=True)

# Plot the probability density function (PDF) of the distribution
pdf = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2))
plt.plot(bins, pdf, linewidth=2, color='r')

plt.show()

