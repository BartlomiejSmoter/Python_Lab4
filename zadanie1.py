def multiply_matrices(matrix_a, matrix_b):

    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Liczba kolumn macierzy A musi być równa liczbie wierszy macierzy B.")

    rows_a = len(matrix_a)
    cols_b = len(matrix_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = multiply_matrices(matrix_a, matrix_b)
for row in result:
    print(row)
