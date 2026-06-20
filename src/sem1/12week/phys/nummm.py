import numpy as np

# Ax = b
# Set up your equations in matrix form
A = np.array([
    [ 1, -1, -1],
    [12, 6,  0],
    [ 0,  -6, 2],
])

b = np.array([0, 18, 12])  # right hand side

x = np.linalg.solve(A, b)

print(f"I  = {x[0]:.4f} A")
print(f"I1 = {x[1]:.4f} A")
print(f"I2 = {x[2]:.4f} A")
