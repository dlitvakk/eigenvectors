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

###
def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues_2, eigenvectors_2 = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors_2, np.diag(eigenvalues_2)), np.linalg.inv(eigenvectors_2))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector

message = "Kostiantyn Derkach is the best boy ever! <3"
key_matrix = np.random.randint(0, 256, (len(message), len(message)))
encrypted_message = encrypt_message(message, key_matrix)
print("Encrypted: ", encrypted_message)



def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues_3, eigenvectors_3 = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors_3, np.diag(eigenvalues_3)), np.linalg.inv(eigenvectors_3))
    diagonalized_key_matrix_inv = np.linalg.inv(diagonalized_key_matrix)
    decrypted_vector = np.dot(diagonalized_key_matrix_inv, encrypted_vector)
    decrypted_message = ''.join([chr(int(round(num.real))) for num in decrypted_vector])
    return decrypted_message


decrypted_message = decrypt_message(encrypted_message, key_matrix)
print("Decrypted: ", decrypted_message)