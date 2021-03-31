import itertools
import numpy as np

def find_cost_brute(arr):
    if len(arr) == 1:
        return 0
    min_idx = np.argmin(arr)
    cost = min_idx + 1
    new_arr = arr[:min_idx][::-1] + arr[min_idx+1:]
    return cost + find_cost_brute(new_arr)


def solve(N, C):
    if not N-1 <= C <= sum(range(2, N+1)):
        return "IMPOSSIBLE"
    l = range(1, N+1)
    for x in itertools.permutations(l):
        if find_cost_brute(x) == C:
            return " ".join(str(_x) for _x in x)


def read():
    num_tc = int(input())
    test_cases = []
    for tc in range(num_tc):
        x, y, = (int(x) for x in input().split(" "))
        test_cases.append((x, y,))
    return test_cases

def print_results(results):
    for idx, res in enumerate(results):
        print("Case #{}: {}".format(idx+1, res))

def main():
    test_cases = read()
    results = [solve(x, y) for x, y in test_cases]
    print_results(results)

if __name__ == '__main__':
    main()

    
