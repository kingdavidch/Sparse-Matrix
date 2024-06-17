def load_sparse_matrix(filename):
    """Reads a sparse matrix from a file in the specified format."""
    with open(filename, 'r') as file:
        rows, cols = [int(file.readline().strip().split('=')[1]) for _ in range(2)]
        matrix = [[0] * cols for _ in range(rows)]
        for line in file:
            if line.strip():
                try:
                    r, c, v = [int(x) for x in line.strip()[1:-1].split(',')]
                    matrix[r - 1][c - 1] = v
                except ValueError:
                    raise ValueError("Incorrect format in input file.")
    return matrix


def perform_matrix_operation(matrix1, matrix2, operation):
    """Performs addition, subtraction, or multiplication of two matrices."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have compatible dimensions.")

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            if operation == 'add':
                result[i][j] = matrix1[i][j] + matrix2[i][j]
            elif operation == 'subtract':
                result[i][j] = matrix1[i][j] - matrix2[i][j]
            elif operation == 'multiply':
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def save_matrix_to_file(matrix, output_file):
    """Writes the matrix to a file in the specified format."""
    with open(output_file, 'w') as file:
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val != 0:  # Only write non-zero values
                    file.write(f"({i + 1}, {j + 1}, {val})\n")


def main():
    """Main function to handle user input and matrix operations."""
    try:
        file1 = input("Input the path of the first file: ")
        file2 = input("Input the path of the second file: ")
        operation = input("What operation do you want to perform [add, subtract, multiply]: ")
        output_file = input("What's the name of the output file: ") or f"matrix_{operation}.txt"

        matrix1 = load_sparse_matrix(file1)
        matrix2 = load_sparse_matrix(file2)

        if operation in ['add', 'subtract', 'multiply']:
            result = perform_matrix_operation(matrix1, matrix2, operation)
            print(f"Matrix {operation}:")
            save_matrix_to_file(result, output_file)

        else:
            raise ValueError("Invalid operation")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
