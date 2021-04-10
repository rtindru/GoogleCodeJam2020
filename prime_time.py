"""
Problem
You are playing a new solitaire game called Prime Time. You are given a deck of cards, and each card has a prime number written on it. Multiple cards may have the same number.

Your goal is to divide the cards into two groups in such a way that the sum of the numbers in the first group is equal to the product of the numbers in the second group. Each card must belong to exactly one of the two groups, and each group must contain at least one card. The sum or product of a group that consists of a single card is simply the number on that card.

Sample Case #1

For example, in the image above, the left group has cards whose sum is 25 and the right group has cards whose product is 25. Therefore, this is a valid split into groups.

Your score is the sum of the numbers in the first group (which is equal to the product of the numbers in the second group), or 0 if you cannot split the cards this way at all. What is the maximum score you can achieve?

Input
The first line of the input gives the number of test cases, T. T test cases follow. The first line of each test case contains a single integer M, representing the number of distinct prime numbers in your deck. Each of the next M lines contains two values: Pi and Ni, representing that you have exactly Ni cards with the prime Pi written on them.

Note that the total number of cards in your deck is the sum of all Nis.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum score you can achieve.

"""
from itertools import combinations
import numpy as np    

def prime_sum(prime_list):
    """
    Naive exhaustive solution
    """
    max_sum = sum(prime_list)
    values = []
    for i in range(len(prime_list), 0, -1):
        for comb in combinations(prime_list, i):
            comb_list = list(comb)
            comb_sum = np.prod(comb)
            if comb_sum < max_sum:
                add_sum = 0
                for item in prime_list:
                    if item in comb_list:
                        comb_list.remove(item)
                    else:
                        add_sum += item
                if add_sum == comb_sum:
                    values.append(add_sum)
    return max(values) if values else 0

def read():
    num_tc = int(input())
    test_cases = []
    for _ in range(num_tc):
        rows = int(input())
        prime_list = []
        for _ in range(rows):
            prime, num = (int(x) for x in input().split(" "))
            prime_list.extend([prime] * num)
        test_cases.append(prime_list)
    return test_cases

def main():
    test_cases = read()
    for idx, tc in enumerate(test_cases):
        res = prime_sum(tc)
        print("Case #{}: {}".format((idx+1), res))

if __name__ == '__main__':
    main()
