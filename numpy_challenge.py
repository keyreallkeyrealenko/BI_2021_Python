import numpy as np


def matrix_multiplication(matrix_1, matrix_2):
    # Function returns multiplication of two matrices
    return np.dot(matrix_1, matrix_2)


def multiplication_check(matrices_list):
    # It returns True when it is possible to multiply all matrices one by one in a given order
    first_matrix = matrices_list[0]
    for i in range(1, len(matrices_list)):
        second_matrix = matrices_list[i]
        try:
            first_matrix = matrix_multiplication(first_matrix, second_matrix)
        except ValueError:
            return None
    return True


def multiply_matrices(matrices_list):
    # Function multiplies matrices one by one in a given order if it is possible
    if multiplication_check(matrices_list):
        first_matrix = matrices_list[0]
        for i in range(1, len(matrices_list)):
            second_matrix = matrices_list[i]
            first_matrix = matrix_multiplication(first_matrix, second_matrix)
        return first_matrix
    return None


def compute_2d_distance(coord1, coord2, plotting=False):
    # This function computes an Euclidean distance between two coordinates
    # Btw for there is an method numpy.linalg.norm() it uses an Euclidean distance
    # by default
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def compute_multidimensional_distance(arr_1, arr_2):
    # Function computes an Euclidean distance between any number of coordinates in
    # arr_1 and arr_2 (size should be equal)
    return np.linalg.norm(arr_1 - arr_2)


def compute_pair_distances(given_matrix):
    # Function creates a pairwise distance matrix (based on Euclidean distance)
    resulted_matrix = []
    shape = given_matrix.shape[0]
    for i in range(len(given_matrix)):
        for j in range(len(given_matrix)):
            resulted_matrix.append(compute_multidimensional_distance(given_matrix[i], given_matrix[j]))
    return np.array(resulted_matrix).reshape(shape, shape)


if __name__ == '__main__':
    # Here yo can see my 3 favourite arrays (Btw I love np.random it doesn't matter which array to choose here):
    arr_eye = np.eye(5, 5)
    arr_random = np.random.randint(0, 10, (3, 3))
    arr_lin = np.linspace(1, 10, 20).reshape(5, 4)
