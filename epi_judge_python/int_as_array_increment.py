from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1
    while i >= 0:
        A[i] += 1
        if A[i] != 10:
            break
        A[i] = 0
        i -= 1
    if A[0] == 0:
        A.insert(0, 1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
