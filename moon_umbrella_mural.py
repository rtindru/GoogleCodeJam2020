def solve(x, y, string):
    prev = None
    cost = 0
    for char in string:
        if char == "J":
            if prev == "C":
                cost += x
            prev = "J"
        elif char == "C":
            if prev == "J":
                cost += y
            prev = "C"
    return cost

def read():
    num_tc = int(input())
    test_cases = []
    for tc in range(num_tc):
        x, y, string = input().split(" ")
        x, y = int(x), int(y)
        test_cases.append((x, y, string))
    return test_cases

def print_results(results):
    for idx, res in enumerate(results):
        print("Case #{}: {}".format(idx+1, res))

def main():
    test_cases = read()
    results = [solve(x, y, string) for x, y, string in test_cases]
    print_results(results)

if __name__ == '__main__':
    main()