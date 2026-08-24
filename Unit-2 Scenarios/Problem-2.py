def generate_fibonacci_tabulation(n):
    """
    Generates the first N Fibonacci numbers using Bottom-Up Dynamic Programming (Tabulation).
    
    Requirements:
    - Accept an integer N.
    - Build the solution iteratively using a DP table.
    - Return/Display the generated sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Step 1: Initialize the DP table of size N
    dp = [0] * n
    
    # Step 2: Set base cases
    dp[0] = 0
    dp[1] = 1

    # Step 3: Build the solution iteratively from bottom-up
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


if __name__ == "__main__":
    try:
        N = int(input("Enter the value of N: "))
        if N < 0:
            print("Please enter a non-negative integer.")
        else:
            sequence = generate_fibonacci_tabulation(N)
            print(f"The first {N} Fibonacci numbers are:")
            print(sequence)
    except ValueError:
        print("Invalid input! Please enter an integer.")

"""
==================================================
SAMPLE OUTPUT / RUNTIME EXECUTION
==================================================

Example 1:
Enter the value of N: 8
The first 8 Fibonacci numbers are:
[0, 1, 1, 2, 3, 5, 8, 13]

Example 2:
Enter the value of N: 1
The first 1 Fibonacci numbers are:
[0]

Example 3:
Enter the value of N: 0
The first 0 Fibonacci numbers are:
[]
==================================================
"""
