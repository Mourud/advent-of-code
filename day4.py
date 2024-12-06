from numpy import mat, matrix
from input_fetcher import fetch_input

def main():
    input = fetch_input(__file__)
    print(part1(input))
    

def part1(input):
    matrix_of_chars = input.splitlines()
    transposed_matrix_of_chars = transpose_matrix(matrix_of_chars)
    horizonals = find_XMAS_hor(matrix_of_chars)
    verticals = find_XMAS_hor(transposed_matrix_of_chars)
    diagoanls = find_XMAS_diagonal(matrix_of_chars)
    return horizonals + verticals + diagoanls

def find_XMAS_diagonal(matrix):
    total = 0
    for i in range(len(matrix) - 3):
        for j in range(len(matrix[0]) - 3):
            X = matrix[i][j]
            M = matrix[i+1][j+1]
            A = matrix[i+2][j+2]
            S = matrix[i+3][j+3]
            x = matrix[i][j+3]
            m = matrix[i+1][j+2]
            a = matrix[i+2][j+1]
            s = matrix[i+3][j]

            if is_diagonal_xmas(X,M,A,S):
                total +=1
            if is_diagonal_xmas(x,m,a,s):
                total+=1

    return total

def is_diagonal_xmas(X, M, A, S):
    return (X == 'X' and M == 'M' and A == 'A' and S == 'S') or (S == 'X' and A == 'M' and M == 'A' and X == 'S')


def find_XMAS_hor(matrix):
    return sum([line.count('XMAS') + line.count('SAMX') for line in matrix])

def transpose_matrix(matrix):
    transpose = [[0 for _ in line] for line in matrix]
    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            transpose[j][i] = c
    for line in transpose:
        line = ''.join(line)
            
    return transpose

main()