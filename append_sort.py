"""
Problem
We have a list of integers X1,X2,…,XN. We would like them to be in strictly increasing order, but unfortunately, we cannot reorder them. This means that usual sorting algorithms will not work.

Our only option is to change them by appending digits 0 through 9 to their right (in base 10). For example, if one of the integers is 10, you can turn it into 100 or 109 with a single append operation, or into 1034 with two operations (as seen in the image below).

Given the current list, what is the minimum number of single digit append operations that are necessary for the list to be in strictly increasing order?

For example, if the list is 100,7,10, we can use 4 total operations to make it into a sorted list, as the following image shows.

Sample Case #1

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case is described in two lines. The first line of a test case contains a single integer N, the number of integers in the list. The second line contains N integers X1,X2,…,XN, the members of the list.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of single digit append operations needed for the list to be in strictly increasing order.

"""

def append(num1, num2, ):
    if num2 > num1:
        return 0, num2
    elif num2 == num1:
        return 1, int(str(num2) + "0")

    str1, str2 = str(num1), str(num2)
    l1, l2 = len(str1), len(str2)
    diff = l1 - l2

    if str1[:l2] == str2:
        postfix = str1[l2:]
        if set(postfix) == set(["9"]):
            append_len = len(postfix) + 1
            append_num = "0" * (diff+1)
        else:
            append_len = len(postfix)
            append_num = int(postfix) + 1
    elif num2 > int(str1[:l2]):
        append_num = "0" * (diff)
        append_len = diff
    else:
        append_num = "0" * (diff+1)
        append_len = diff+1

    return append_len, int(str(num2) + str(append_num))


def append_count(num_list, ):
    total = 0
    prev = num_list[0]
    for num in num_list[1:]:
        append_len, append_num = append(prev, num)
        total += append_len
        prev = append_num
    return total

def read():
    num_tc = int(input())
    test_cases = []
    for _ in range(num_tc):
        _ = int(input())
        test_cases.append([int(x) for x in input().split(" ")])
    return test_cases

def main():
    test_cases = read()
    for idx, tc in enumerate(test_cases):
        res = append_count(tc)
        print("Case #{}: {}".format((idx+1), res))

if __name__ == '__main__':
    main()
