import numpy as np

#array 
a = np.array(list(range(1,5,1)))
b = np.array(list(range(5,10,1)))



def print_array_details(): 
    print("Dimensions: %d, shape: %s, dtypes: %s "%(a.ndim, a.shape, a.dtype))

print(print_array_details())

# Addition
c = a + b
print(c)  # [5 7 9]

# Subtraktion
d = a - b
print(d)  # [-3 -3 -3]

# Elementweise Multiplikation
e = a * b
print(e)  # [ 4 10 18]

# Elementweise Division
f = a / b
print(f)  # [0.25 0.4 0.5]

# Exponentiation
g = a ** 2
print(g)  # [1 4 9]

# Summe aller Elemente
print(a.sum())  # 6

# Mittelwert
print(a.mean())  # 2.0



