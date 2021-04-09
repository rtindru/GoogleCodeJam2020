"""
Problem
Many terminals use asterisks (*) to signify "any string", including the empty string. For example, when listing files matching BASH*, a terminal may list BASH, BASHER and BASHFUL. For *FUL, it may list BEAUTIFUL, AWFUL and BASHFUL. When listing B*L, BASHFUL, BEAUTIFUL and BULL may be listed.

In this problem, formally, a pattern is a string consisting of only uppercase English letters and asterisks (*), and a name is a string consisting of only uppercase English letters. A pattern p matches a name m if there is a way of replacing every asterisk in p with a (possibly empty) string to obtain m. Notice that each asterisk may be replaced by a different string.

Given N patterns, can you find a single name of at most 104 letters that matches all those patterns at once, or report that it cannot be done?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line with a single integer N: the number of patterns to simultaneously match. Then, N lines follow, each one containing a single string Pi representing the i-th pattern.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is any name containing at most 104 letters such that each Pi matches y according to the definition above, or * (i.e., just an asterisk) if there is no such name.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 50.
2 ≤ length of Pi ≤ 100, for all i.
Each character of Pi is either an uppercase English letter or an asterisk (*), for all i.
At least one character of Pi is an uppercase English letter, for all i.

Test set 1 (Visible Verdict)
Exactly one character of Pi is an asterisk (*), for all i.
The leftmost character of Pi is the only asterisk (*), for all i.
Test set 2 (Visible Verdict)
Exactly one character of Pi is an asterisk (*), for all i.
Test set 3 (Visible Verdict)
At least one character of Pi is an asterisk (*), for all i.

"""
def merge_starts(s1, s2):
    if len(s1) == len(s2):
        return s1 if s1 == s2 else False
    long_str = s1 if len(s1) > len(s2) else s2
    short_str = s1 if len(s1) < len(s2) else s2
    return long_str if long_str[:len(short_str)] == short_str else False

def merge_ends(s1, s2):
    if len(s1) == len(s2):
        return s1 if s1 == s2 else False
    long_str = s1 if len(s1) > len(s2) else s2
    short_str = s1 if len(s1) < len(s2) else s2
    return long_str if long_str[-len(short_str):] == short_str else False

def merge(*strings):
    startswith = ''
    endswith = ''
    contains = []

    for string in strings:
        subs_strings = string.split("*")  # ["H", "O"]
        for i, s1 in enumerate(subs_strings):
            if s1 == '':
                continue
            if i == 0:
                if startswith == '':
                    startswith = s1
                else:
                    startswith = merge_starts(s1, startswith)
                if startswith is False:
                    return "*"
            elif i == len(subs_strings)-1:
                if endswith == '':
                    endswith = s1
                else:
                    endswith = merge_ends(s1, endswith)
                if endswith is False:
                    return "*"
            else:
                contains.append(s1)
        # print("{}: Start: {}, End: {}, Contain: {}".format(string, startswith, endswith, contains))
    return gen_str(startswith, endswith, contains)

def gen_str(startswith, endswith, contains):
    if not contains:
        if startswith == endswith:
            return startswith
        else: 
            return startswith + endswith
    else:
        return startswith + "".join(contains) + endswith

def read():
    num_tc = int(input())
    test_cases = []
    for tc in range(num_tc):
        num_strs = int(input())
        strings = []
        for i in range(num_strs):
            strings.append(input())
        test_cases.append(strings)
    return test_cases

def print_results(results):
    for idx, res in enumerate(results):
        print("Case #{}: {}".format(idx+1, res))

def main():
    test_cases = read()
    results = [merge(*strings) for strings in test_cases]
    print_results(results)

if __name__ == '__main__':
    main()