# Algo-programming-assignment-3

Name: Tiffany Dang (UFID: 14332676)

• Instructions to compile/build your code (if applicable).
• Instructions to run the code that runs each of the eviction policies, including
example commands.
• Any assumptions (input/output format, dependencies, etc.).
• Your solution to the written component, i.e., Questions 1, 2, and 3.

## Question 1: Empirical Comparison

## Question 2: Recurrence Equation

### Def. dp[i][j] = max value common subsequence of A[1, …, i] and B[1, …, j].

Base cases: dp[0][j] = 0 and dp[i][0] = 0 (if either prefix is empty, no common subsequence)
Case 1: A[i] = B[j] => the characters match.

Can extend the best solution for A[1…i-1] and B[1…j-1] by appending this character, adding v(A[i])


Case 2: A[i] ≠ B[j] => the characters don't match.

Either skip A[i] → look at dp[i-1][j]
Or skip B[j] → look at dp[i][j-1]
Take the better one.

### Recurrence eq:

dp [i][j] = {
    dp [i-1][j-1] + v(A[i])           if A[i] = B[j]
    max(dp [i-1][j], dp [i][j-1])     otherwise
}

## Question 3: Big-O
