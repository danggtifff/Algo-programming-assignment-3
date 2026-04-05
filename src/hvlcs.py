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
"""