import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size=(dim, dim))
    return matrix
def generate_permutations(n):
    """
    функція створення списку перестановок.
    """
    return list(itertools.permutations(range(n)))
def product_of_permutation(matrix, perm):
    """
    функція підрахунку добутків.
    """
    product = 1
    for i in range(len(matrix)):
        product *= matrix[i][perm[i]]
    return product
def determinant_by_permutations(matrix):
    """
    функція підрахунку загальної суми.
    """
    n = len(matrix)
    permutations = generate_permutations(n)
    det = 0
    for perm in permutations:
        sign = (-1) ** sum(i < j and perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        det += sign * product_of_permutation(matrix, perm)
    return det
while True:
    try:
        n = int(input("Введіть розмірність матриці (ціле додатнє число): "))
        if n > 0:
            break
        else:
            print("Будь ласка, введіть ціле додатнє число.")
    except ValueError:
        print("Невірний ввід. Будь ласка, введіть ціле додатнє число.")
matrix = random_matrix(n)
print("Згенерована матриця:")
print(matrix)
determinant = determinant_by_permutations(matrix)
print(determinant)
numpy_determinant = np.linalg.det(matrix)
print(numpy_determinant)
