import numpy as np
import sys

# We're aiming for 100MB array. As each float64 takes 8 bytes, we'll need 12.5 million elements.
num_elements = 12500000

# Create a numpy array with the specified number of elements
array = np.random.random(num_elements)

# Print the size of the array in bytes
print('Array size in bytes:', sys.getsizeof(array))

# Print the size of the array in megabytes
print('Array size in MB:', sys.getsizeof(array) / (1024 * 1024))