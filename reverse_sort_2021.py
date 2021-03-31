"""
Problem
Note: The main parts of the statements of the problems "Reversort" and "Reversort Engineering" are identical, except for the last paragraph. The problems can otherwise be solved independently.

Reversort is an algorithm to sort a list of distinct integers in increasing order. The algorithm is based on the "Reverse" operation. Each application of this operation reverses the order of some contiguous part of the list.

The pseudocode of the algorithm is the following:

Reversort(L):
  for i := 1 to length(L) - 1
    j := position with the minimum value in L between i and length(L), inclusive
    Reverse(L[i..j])
After i−1 iterations, the positions 1,2,…,i−1 of the list contain the i−1 smallest elements of L, in increasing order. During the i-th iteration, the process reverses the sublist going from the i-th position to the current position of the i-th minimum element. That makes the i-th minimum element end up in the i-th position.

For example, for a list with 4 elements, the algorithm would perform 3 iterations. Here is how it would process L=[4,2,1,3]:

L=[4,2,1,3]
i=1, j=3⟶L=[1,2,4,3] => 3
i=2, j=2⟶L=[1,2,4,3] => 1
i=3, j=4⟶L=[1,2,3,4] => 2

[1, 2, 3, 4]
[3, 2, 4, 1] --> [3, 1, 2] --> 6

(-2, 0, -1, 3) => 6


i=N; j=N: [7, 3, 5, 9, 2]
i=1, j=5: [2, 9, 5, 3, 7] => 5
i=2, j=4: [2, 3, 5, 9, 7] => 3
i=3, j=3: [2, 3, 5, 9, 7] => 1
i=4, j=5: [2, 3, 5, 7, 9] => 2
Total: 11

[1, 2, 3, 4, 5]
[5, 2, 3, 1, 4] --> [5, 3, 1, 2] => 11

---
[4, 3, 2]
[3, 2, 1] => [3, 1] => 4

1, 3, [2, 3, 4] => 3
2, 2, [2, 3, 4] => 1
---
          [5, 2, 4, 3]
i=1, j=2: [2, 5, 4, 3] => 2
i=2, j=4: [2, 3, 4, 5] => 3
i=3, j=3: [2, 3, 4, 5] => 1

[1, 2, 3, 4]
[2, 4, 3, 1] --> [2, 2, 1] ==> 5
---
         [5, 2, 4, 1, 3]
i=1, j=4: [1, 4, 2, 5, 3] => 4
i=2, j=3: [1, 2, 4, 5, 3] => 2
i=3, j=5: [1, 2, 3, 4, 5] => 3
i=4, j=4: [1, 2, 3, 4, 5] => 1

[1, 2, 3, 4, 5]
[4, 2, 5, 1, 3] -> [4, 2, 3, 4] 

[1, 2, 3, 4]
[4, (5-2+1), 5, (5-3+1)]

---
i=N; j=N: [7, 6, 5, 4, 3]
i=1, j=5: [3, 4, 5, 6, 7] => 5
i=2, j=2: [3, 4, 5, 6, 7] => 1
i=3, j=3: [3, 4, 5, 6, 7] => 1
i=4, j=4: [3, 4, 5, 6, 7] => 1
Total: 8

[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1] --> [5, 1, 1, 1, ] => 8
[1, 2, 3, 4, 5]


i=1, j=3⟶L=[1,2,4,3]
i=2, j=2⟶L=[1,2,4,3]
i=3, j=4⟶L=[1,2,3,4]
The most expensive part of executing the algorithm on our architecture is the Reverse operation. Therefore, our measure for the cost of each iteration is simply the length of the sublist passed to Reverse, that is, the value j−i+1. The cost of the whole algorithm is the sum of the costs of each iteration.

In the example above, the iterations cost 3, 1, and 2, in that order, for a total of 6.

Given the initial list, compute the cost of executing Reversort on it.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 2 lines. The first line contains a single integer N, representing the number of elements in the input list. The second line contains N distinct integers L1, L2, ..., LN, representing the elements of the input list L, in order.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the total cost of executing Reversort on the list given as input.

Limits
Time limit: 10 seconds.
Memory limit: 1 GB.
Test Set 1 (Visible Verdict)
1≤T≤100.
2≤N≤100.
1≤Li≤N, for all i.
Li≠Lj, for all i≠j.
"""



import numpy as np

def find_cost_brute(arr):
    if len(arr) == 1:
        return 0
    min_idx = np.argmin(arr)
    cost = min_idx + 1
    new_arr = arr[:min_idx][::-1] + arr[min_idx+1:]
    return cost + find_cost_brute(new_arr)

def read():
    num_tc = int(input())
    test_cases = []
    for tc in range(num_tc):
        list_len = int(input())
        list_val = [int(x) for x in input().split(" ")]
        test_cases.append((list_len, list_val))
    return test_cases

def print_results(results):
    for idx, res in enumerate(results):
        print("Case #{}: {}".format(idx+1, res))

def main():
    test_cases = read()
    results = [find_cost_brute(arr) for _, arr in test_cases]
    print_results(results)

if __name__ == '__main__':
    main()
