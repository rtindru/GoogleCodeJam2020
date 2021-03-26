import numpy as np

def read():
    test_cases = int(input())
    matrices = [None] * test_cases
    for tc in range(test_cases):
        n = int(input())
        matrix = np.empty([n, n])
        for i in range(n):
            row = input()
            row = [int(x) for x in row.split(" ")]
            matrix[i] = row
        matrices[tc] = matrix
    return matrices


def count_dups(m):
    d = 0
    for row in m:
        s = set()
        for item in row:
            if item in s:
                d += 1
                break
            else:
                s.add(item)
    return d

def process_matrix(m):
    r = count_dups(m)
    c = count_dups(m.transpose())
    t = int(np.sum(np.diagonal(m)))
    return t, r, c

def print_out(res):
    for idx, (t, r, c) in enumerate(res):
        print("Case #{}: {} {} {}".format(idx+1, t, r, c))

def run():
    matrices = read()
    res = [process_matrix(m) for m in matrices]
    print_out(res)

run()