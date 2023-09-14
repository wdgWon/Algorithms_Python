n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
items = [[0, 0]]

for _ in range(n):
    items.append(list(map(int,input().split())))

for i in range(1, n+1):
    for j in range(k, 0, -1):
        if items[i][0] <= j:
            dp[j] = max(dp[j], dp[j-items[i][0]] + items[i][1])

print(dp[k])
