"""
Highest Value Longest Common Subsequence (HVLCS)
"""

"""
Def. dp[i][j] = max value common subsequence of A[1, …, i] and B[1, …, j].

Base cases: dp[0][j] = 0 and dp[i][0] = 0 (if either prefix is empty, no common subsequence)
Case 1: A[i] = B[j] => the characters match.

Can extend the best solution for A[1…i-1] and B[1…j-1] by appending this character, adding v(A[i])


Case 2: A[i] ≠ B[j] => the characters don't match.

Either skip A[i] → look at dp[i-1][j]
Or skip B[j] → look at dp[i][j-1]
Take the better one.

Recurrence eq:

dp [i][j] = {
    dp [i-1][j-1] + v(A[i])           if A[i] = B[j]
    max(dp [i-1][j], dp [i][j-1])     otherwise
}
"""

"""
Sources:
https://medium.com/@prajun_t/dynamic-programming-longest-common-subsequence-lcs-7884b0540638
https://ics.uci.edu/~goodrich/teach/cs260P/notes/LCS.pdf
https://www.khoury.northeastern.edu/home/vip/teach/Algorithms/6_dyn_prog/notes/LCS/LCS.pdf
"""

import sys

def solve(input_text: str) -> tuple[int, str]:
    # parse the input text
    lines = input_text.strip().split("\n")
    idx = 0
    
    K = int(lines[idx].strip())
    idx += 1

    char_value = {}
    for i in range(K):
        parts = lines[idx].strip().split()
        char = parts[0]
        val = int(parts[1])
        char_value[char] = val
        idx += 1
 
    A = lines[idx].strip()
    idx += 1
    B = lines[idx].strip()
 
    m = len(A)
    n = len(B)

    # create dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                # dp [i-1][j-1] + v(A[i])           if A[i] = B[j]
                dp[i][j] = dp[i - 1][j - 1] + char_value.get(A[i - 1], 0)
            else:
                # max(dp [i-1][j], dp [i][j-1])     otherwise
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
 
    result.reverse()
    subsequence = "".join(result)
    max_value = dp[m][n]
 
    return max_value, subsequence

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
 
    max_value, subsequence = solve(input_text)
    print(max_value)
    print(subsequence)
 
 
if __name__ == "__main__":
    main()