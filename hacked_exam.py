"""
Problem
There is an exam with Q true or false questions. The correct answer to each question is either T or F. Each student taking the exam selects either T or F for each question, and the student's score is the number of questions they answer correctly.

Example Exam

There are N students who have already taken this exam. For each of those students, you know the answers they gave to each question and their final score. Assuming that any sequence of answers that is consistent with all of those students' scores has the same probability of being the correct sequence of answers, you want to maximize your own expected score. Determine what that expected score is and how to answer the questions so that you achieve it.

Input
The first line of the input gives the number of test cases, T. T test cases follow. The first line of each test case contains two integers N and Q: the number of students and the number of questions, respectively. Each of the next N lines contains a string Ai and an integer Si: the i-th student's answers and their score, respectively. The j-th character of Ai is either T or F, representing the answer the i-th student gave to the j-th question.

Output
For each test case, output one line containing Case #x: y z/w, where x is the test case number (starting from 1), y is a string representing a sequence of answers that yields the maximum expected score (in the same format as the input), and zw is the maximum expected score as an irreducible fraction (that is, w must be positive and of minimum possible value).

"""

from itertools import combinations

def invert(ans):
    if ans == "T":
        return "F"
    return "T"

def gen_combos(keystr, num_right):
    size = len(keystr)
    combos = combinations(range(size), num_right)
    for combo in combos:
        res = []
        for i in range(size):
            og_ans = keystr[i]
            if i in combo:
                res.append(og_ans)
            else:
                res.append(invert(og_ans))
        yield "".join(res)

def solve(strings):
    size = len(strings[0][0])
    all_combos = []
    for string, score in strings:
        combos = gen_combos(string, score)
        all_combos.append(set(combos))

    vals = set.intersection(*all_combos)
    from collections import defaultdict
    d = defaultdict(int)
    for val in vals:
        for idx, c in enumerate(val):
            if c == "T":
                d[idx] += 1
    from fractions import Fraction
    def get_mid(size):
        if size % 2 == 0:
            return size / 2
        return (size + 1) / 2

    vallen = len(vals)
    mid = get_mid(vallen)
    res = []
    probs = []
    for i in range(size):
        if d[i] >= mid:
            res.append('T')
            probs.append(d[i])
        else:
            res.append('F')
            probs.append(vallen-d[i])
    return "".join(res), Fraction(sum(probs), vallen)


def read():
    num_tc = int(input())
    test_cases = []
    for _ in range(num_tc):
        rows, _ = (int(x) for x in input().split(" "))
        tc = []
        for _ in range(rows):
            instr = input()
            x, y = instr.split(" ")
            y = int(y)
            tc.append((x, y))
        test_cases.append(tc)

    return test_cases

def main():
    test_cases = read()
    for idx, tc in enumerate(test_cases):
        res = solve(tc)
        print("Case #{}: {} {}/{}".format((idx+1), res[0], res[1].numerator, res[1].denominator))

if __name__ == '__main__':
    main()