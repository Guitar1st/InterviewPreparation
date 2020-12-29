"""
TODO: check solution, write tests
"""


def dp_recursive(k, arr, memo):
    max_subsol = 0
    if k > 0:
        for i in arr:
            if k - i in memo:
                subsol = memo[k - i] + i
            else:
                subsol = dp_recursive(k - i, arr, memo) + i
            # print("Subsol dp({}) = {}".format(k, subsol))
            if max_subsol < subsol <= k:
                max_subsol = subsol
                memo[k] = subsol
    return max_subsol


def dp_bottom_up(k, arr, memo):
    max_subsol = 0
    for j in range(1, k+1):
        for i in arr:
            subsol = memo.get(j - i, 0) + i
            if max_subsol < subsol <= j:
                max_subsol = subsol
        memo[j] = max_subsol
    return memo[k]


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().strip().split(' '))
        arr = list(map(int, input().strip().split(' ')))
        memo = {0: 0}
        result = dp_bottom_up(k, arr, memo)
        print(result)
