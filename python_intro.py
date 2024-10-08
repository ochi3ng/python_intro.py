# 1) Garbage Collection in Python

# Garbage collection (GC) in Python is a mechanism to automatically manage memory
# by reclaiming memory that is no longer in use, specifically memory allocated to objects
# that are no longer referenced. Python uses reference counting and a cyclic garbage collector
# to handle this.

# Reference Counting:
# Each object in Python has a reference count, which tracks the number of references to that object.
# When an object's reference count drops to zero (i.e., it’s no longer referenced anywhere),
# Python automatically deallocates the memory.

# Cyclic Garbage Collector:
# Python can also detect and clean up circular references—where two or more objects reference each other
# but are otherwise unreachable.

# Example of triggering garbage collection:
import gc
gc.collect()  # Triggers the garbage collection process


# 2) Differences between NumPy Arrays and Python Lists

import numpy as np

# NumPy arrays vs Python lists
# Feature               | NumPy Array                            | Python List
# --------------------- | -------------------------------------- | -----------
# Memory                | More efficient (stores data contiguously) | Less efficient (stores pointers to objects)
# Data Types            | Homogeneous (same type)                | Heterogeneous (can store different types)
# Speed                 | Faster for numerical operations        | Slower
# Operations            | Supports vectorized operations         | Requires loops

# Example of NumPy array:
arr = np.array([1, 2, 3, 4])
result = arr * 2  # Element-wise multiplication
print(result)  # Output: [2 4 6 8]


# 3) List Comprehension in Python

# List comprehension is a concise way to create lists.

# Example of generating squared values:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example of filtering based on a condition:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


# 4) Shallow vs. Deep Copying in Python

import copy

# Shallow Copy: Creates a new object, but references the original nested objects.
# Deep Copy: Creates a completely independent copy of the object and all nested objects.

original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow_copy = copy.copy(original)
shallow_copy[0][0] = 99
print(original[0][0])  # Output: 99 (nested objects share memory)

# Deep copy
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 100
print(original[0][0])  # Output: 99 (deep copy doesn't affect the original)


# 5) Difference between Lists and Tuples

# Mutability: Lists are mutable, meaning you can modify, add, or remove elements after creation.
# Tuples are immutable, meaning once created, their content cannot be changed.

# List (mutable)
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the list
print(my_list)  # Output: [10, 2, 3]

# Tuple (immutable)
my_tuple = (1, 2, 3)
# Uncommenting the following line will raise an error
# my_tuple[0] = 10  # Tuples cannot be modified
print(my_tuple)  # Output: (1, 2, 3)
