#Assignment : 6
def knap_bottom(wt, val, cap):
    n = len(wt)
    dp = [[0 for c in range(cap + 1)] for r in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, cap + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    chosen = []
    w = cap
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i)
            w = w - wt[i - 1]
    chosen.reverse()

    return dp[n][cap], chosen


def knap_top(wt, val, cap):
    n = len(wt)
    memo = [[-1 for c in range(cap + 1)] for r in range(n + 1)]

    def solve(i, w):
        if i == 0 or w == 0:
            return 0
        if memo[i][w] != -1:
            return memo[i][w]
        if wt[i - 1] > w:
            memo[i][w] = solve(i - 1, w)
        else:
            take = val[i - 1] + solve(i - 1, w - wt[i - 1])
            skip = solve(i - 1, w)
            memo[i][w] = max(take, skip)
        return memo[i][w]

    best = solve(n, cap)

    chosen = []
    w = cap
    for i in range(n, 0, -1):
        if solve(i, w) != solve(i - 1, w):
            chosen.append(i)
            w = w - wt[i - 1]
    chosen.reverse()

    return best, chosen


weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
bag_capacity = 5

print("0/1 knapsack problem")
print("Items in the bag:")
for i in range(len(weights)):
    print("Item", i + 1, ": weight =", weights[i], ", value =", values[i])

print("Bag capacity:", bag_capacity)

ans1, picked1 = knap_bottom(weights, values, bag_capacity)
print("Bottom up result")
print("Max value:", ans1)
print("Items picked:", picked1)

ans2, picked2 = knap_top(weights, values, bag_capacity)
print("Top down result")
print("Max value:", ans2)
print("Items picked:", picked2)

#Output
'''0/1 knapsack problem
Items in the bag:
Item 1 : weight = 2 , value = 10
Item 2 : weight = 1 , value = 10
Item 3 : weight = 3 , value = 20
Item 4 : weight = 2 , value = 15
Bag capacity: 5
Bottom up result
Max value: 37
Items picked: [1, 2, 4]
Top down result
Max value: 37
Items picked: [1, 2, 4]'''