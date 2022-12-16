#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    arr = []
    k = 0
    for i in matrix:
        arr.append([])
        for j in i:
            arr[k].append((j ** 2))
        k = k + 1
    return (arr)
