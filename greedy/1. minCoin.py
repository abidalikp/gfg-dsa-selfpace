#Not always feasible
def minCoin(coins, amount):
    balance = amount
    coins.sort(reverse=True)
    ans = 0
    for coin in coins:
        ans += balance//coin
        balance = balance%coin
    return ans

#main:

coins = [10, 5, 2, 1]
amount = 58

res = minCoin(coins, amount)

print(res)