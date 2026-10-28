import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    D = len(A)
    N = len(A[0])

    arr = np.zeros((N, D))
    for i in range(len(A)):
        for j in range(len(A[i])):
            arr[j][i] = A[i][j]
    return arr
    pass
