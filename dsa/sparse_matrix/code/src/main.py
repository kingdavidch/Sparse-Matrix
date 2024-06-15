def SparseMatrix(filename):
    with open(filename, 'r') as file:
        rows = int(file.readline().strip().split('=')[1])
        cols = int(file.readline().strip().split('=')[1])
        matrix = [[0] * cols for _ in range(rows)]

        for line in file:
            entry = line.strip()
            if entry:
                try:
                    r, c, v = map(int, entry[1:-1].split(','))
                    matrix[r-1][c-1] = v
                except Exception:
                    raise Exception("Input file has wrong format")

    return matrix


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[None] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


def subtract_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[None] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] - matrix2[i][j]

    return result


def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])
    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def solve_matrix_sum(file1, file2):
    # Read matrices from files
    matrix1 = SparseMatrix(file1)
    matrix2 = SparseMatrix(file2)

    # Ensure matrices have the same dimensions for addition
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition")

    # Perform arithmetic operations
    matrix_sum = add_matrices(matrix1, matrix2)

    return matrix_sum


def solve_matrix_diff(file1, file2):
    # Read matrices from files
    matrix1 = SparseMatrix(file1)
    matrix2 = SparseMatrix(file2)

    # Ensure matrices have the same dimensions for subtraction
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction")

    # Perform arithmetic operations
    matrix_diff = subtract_matrices(matrix1, matrix2)

    return matrix_diff


def solve_matrix_product(file1, file2):
    # Read matrices from files
    matrix1 = SparseMatrix(file1)
    matrix2 = SparseMatrix(file2)

    # Ensure the matrices are compatible for multiplication
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices must have compatible dimensions for multiplication")

    matrix_product = multiply_matrices(matrix1, matrix2)

    return matrix_product


def write_to_file(matrix, output_file):
    with open(output_file, 'w') as file:
        for index, row in enumerate(matrix):
            for index, col in enumerate(row):
                if col != None:
                    file.write(f"({index+1}, {index+1}, {col})\n")


if __name__ == "__main__":
    try:
        first_file = input("Input the path of the first file: ")
        second_file = input("Input the path of the second file: ")
        operation = input("What operation do you want to perform [add, subtract, multiply]: ")
        output_file = input("What's the name of the output file: ")

        if operation not in ['add', 'subtract', 'multiply']:
            raise ValueError("Invalid operation")

        elif operation == 'add':
            matrix_sum = solve_matrix_sum(first_file, second_file)
            print("Matrix Sum:")
            if not output_file:
                output_file = 'matrix_sum.txt'
            write_to_file(matrix_sum, output_file)

        elif operation == 'subtract':
            matrix_diff = solve_matrix_diff(first_file, second_file)
            print("Matrix Difference:")
            if not output_file:
                output_file = 'matrix_diff.txt'
            write_to_file(matrix_diff, output_file)

        else:
            matrix_product = solve_matrix_product(first_file, second_file)
            print("Matrix Product:")
            if not output_file:
                output_file = 'matrix_product.txt'
            write_to_file(matrix_product, output_file)

    except Exception as ex:
        print(f"Error: {ex}")
