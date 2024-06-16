import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt

matrix = np.array([[2, -3, 0], [2, -5, 0], [0, 0, 3]])
print(matrix)

[eigenvalues, eigenvectors] = np.linalg.eig(matrix)
# print(eigenvalues)
# print(eigenvectors)

i = 0
for eigenvalue in eigenvalues:
    print(f"The eigenvalue #{i + 1} is {eigenvalue}")
    print(f"The corresponding eigenvector is is:\n{eigenvectors[:, i - 1]}")
    i += 1

    # check
    # matrix * eigenvector = eigenvalue * eigenvector
    av = matrix @ eigenvectors[:, i - 1]
    xv = eigenvectors[:, i - 1] * eigenvalue

    print(f"A⋅v = {av}")
    print(f"λ⋅v = {xv}")

    if np.allclose(av,
                   xv):
        print("The calculations are correct! ;)")
    else:
        print("Oops! The calculations are incorrect! :(")
    print("\n")

