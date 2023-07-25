def print_matrix_integer(matrix=[[]]):
        for row in range(len(matrix)):
            print(("{}").format(' '.join(str(x) for x in matrix[row]))) 
