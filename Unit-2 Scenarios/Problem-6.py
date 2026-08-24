def count_ways_to_make_change(coins: list[int], target_amount: int) -> int:
    """
    Calculates the total number of combinations to make `target_amount`
    using the given coin denominations using Dynamic Programming.
    """
    # dp[i] will store the number of ways to make amount 'i'
    dp = [0] * (target_amount + 1)

    # Base case: There is 1 way to make amount 0 (using no coins)
    dp[0] = 1

    # Outer loop over coins ensures each combination is counted only once (no permutations)
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            dp[amount] += dp[amount - coin]

    return dp[target_amount]


def main():
    print("=" * 45)
    print("       COIN CHANGE COMBINATIONS (DP)")
    print("=" * 45)

    try:
        raw_coins = input("Enter coin denominations (space-separated): ").strip()
        coins = [int(c) for c in raw_coins.split() if int(c) > 0]
        
        if not coins:
            print("Error: Please provide at least one valid positive coin denomination.")
            return

        target_amount = int(input("Enter target amount: ").strip())

        if target_amount < 0:
            print("Error: Target amount cannot be negative.")
            return

        total_ways = count_ways_to_make_change(coins, target_amount)

        print("-" * 45)
        print(f"Denominations : {coins}")
        print(f"Target Amount : {target_amount}")
        print(f"Total Ways    : {total_ways}")
        print("=" * 45)

    except ValueError:
        print("Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    main()

Output
       COIN CHANGE COMBINATIONS (DP)

Enter coin denominations (space-separated): 1 2 5
Enter target amount: 5

Denominations : [1, 2, 5]
Target Amount : 5
Total Ways    : 4
