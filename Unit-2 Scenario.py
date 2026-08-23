# Coin Change Problem
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))


dp = [float('inf')] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print("Amount cannot be made with given coins.")
else:
    print("Minimum number of coins:", dp[amount])

    '''
    Output

    Enter coin denominations: 1 6 8
    Enter target amount: 16
    Minimum number of coins: 2
    
    '''





# Unique Paths Problem
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))


dp = [[0] * columns for _ in range(rows)]

for i in range(rows):
    dp[i][0] = 1

for j in range(columns):
    dp[0][j] = 1

for i in range(1, rows):
    for j in range(1, columns):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print("Total number of unique paths:", dp[rows - 1][columns - 1])

'''
Output

Enter number of rows: 3
Enter number of columns: 3
Total number of unique paths: 6

'''
