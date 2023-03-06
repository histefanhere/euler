#!/usr/bin/env python3
"""Project Euler #81 - Path sum: two ways (06/03/2023)"""

def get_input():
    with open('resources/p082_matrix.txt', 'r') as file:
        return [[int(x) for x in line.split(',')] for line in file.read().splitlines()]

def solve(matrix):
    # Useful observation: matrix is square
    n = len(matrix)

    # First, sum the top and left edges
    for i in range(1, n):
        matrix[0][i] += matrix[0][i - 1]
        matrix[i][0] += matrix[i - 1][0]

    # Then run the algorithm on the rest of the matrix
    for i in range(1, n):
        for j in range(1, n):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]

if __name__ == "__main__":
    print(solve(get_input()))
