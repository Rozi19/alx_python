def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        new_element = []
        for element in row:
            new_element.append(element ** 2)
        new_list.append(new_element)
    return new_list
