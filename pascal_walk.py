"""
Problem
Pascal's triangle consists of an infinite number of rows of an increasing number of integers each, arranged in a triangular shape.

Let us define (r, k) as the k-th position from the left in the r-th row, with both r and k counted starting from 1. Then Pascal's triangle is defined by the following rules:

The r-th row contains r positions (r, 1), (r, 2), ..., (r, r).
The numbers at positions (r, 1) and (r, r) are 1, for all r.
The number at position (r, k) is the sum of the numbers at positions (r - 1, k - 1) and (r - 1, k), for all k with 2 ≤ k ≤ r - 1.
The first 5 rows of Pascal's triangle look like this:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

In this problem, a Pascal walk is a sequence of s positions (r1, k1), (r2, k2), ..., (rs, ks) in Pascal's triangle that satisfy the following criteria:

r1 = 1 and k1 = 1.
Each subsequent position must be within the triangle and adjacent (in one of the six possible directions) to the previous position. That is, for all i ≥ 1, (ri + 1, ki + 1) must be one of the following that is within the triangle: (ri - 1, ki - 1), (ri - 1, ki), (ri, ki - 1), (ri, ki + 1), (ri + 1, ki), (ri + 1, ki + 1).
No position may be repeated within the sequence. That is, for every i ≠ j, either ri ≠ rj or ki ≠ kj, or both.
Find any Pascal walk of S ≤ 500 positions such that the sum of the numbers in all of the positions it visits is equal to N. It is guaranteed that at least one such walk exists for every N.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each consists of a single line containing a single integer N.

Output
For each test case, first output a line containing Case #x:, where x is the test case number (starting from 1). Then, output your proposed Pascal walk of length S ≤ 500 using S additional lines. The i-th of these lines must be ri ki where (ri, ki) is the i-th position in the walk. For example, the first line should be 1 1 since the first position for all valid walks is (1, 1). The sum of the numbers at the S positions of your proposed Pascal walk must be exactly N.

"""

import numpy as np

graph = [[1], ]

class Graph(list):
    def __init__(self):
        self.graph = [[1], ]
        self.rows = 1

    def add_row(self):
        prev_row = self.graph[-1]
        next_row = [1, ]
        for idx in range(1, len(prev_row)):
            next_row.append(prev_row[idx] + prev_row[idx-1])
        next_row.append(1)
        self.graph.append(next_row)
        self.rows += 1

    def get(self, i, j):
        while self.rows < i:
            self.add_row()
        return self.graph[i-1][j-1]        


def get_neighbors(node):
    def filt(neighbor):
        x, y = neighbor
        return x > 0 and y > 0 and y <= x

    i, j = node
    vals = [(i-1, j), (i+1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1)]
    vals = filter(filt, vals)
    return vals

def walk(target, graph, node=(1, 1), visited=None, runsum=0, recdepth=1):
    if visited is None:
        visited = set()
    
    visited.add(node)
    runsum += graph.get(*node)
    diff = target - runsum
    if runsum == target:
        return [node]

    neighbors = get_neighbors(node)
    explore = []
    for nn in neighbors:
        if nn in visited:
            continue
        elif graph.get(*nn) > diff:
            visited.add(nn)
            continue
        else:
            explore.append(nn)

    if not explore or recdepth >= 500:
        return None  # Dead end, backtrack

    # Visit the larges neighbor first
    explore_vals = [graph.get(*nn) for nn in explore]
    explore_idxs = np.argsort(explore_vals)[::-1]
    for idx in explore_idxs:
        nn = explore[idx]
        res = walk(target, graph, nn, visited, runsum, recdepth+1)
        if res is not None:
            return [node] + res

def read():
    num_tc = int(input())
    test_cases = []
    for _ in range(num_tc):
        target = int(input())
        test_cases.append(target)
    return test_cases

def print_path(idx, path):
    print("Case #{}:".format(idx+1))
    for x, y in path:
        print("{} {}".format(x, y))

def main():
    test_cases = read()
    graph = Graph()
    for idx, target in enumerate(test_cases):
        path = walk(target, graph, )
        print_path(idx, path)

if __name__ == '__main__':
    main()