def optimal1(game, i, j, S):
    if i+1 == j: return max(game[i], game[j])
    return max(S - optimal1(game, i+1, j, S-game[i]),
                S - optimal1(game, i, j-1, S-game[i]))

def optimal2(game, i, j):
    if i+1 == j: return max(game[i], game[j])
    return max(game[i] + min(optimal2(game, i+2, j),
                                optimal2(game, i+1, j-1)),
                game[j] + min(optimal2(game, i+1, j-1),
                                optimal2(game, i, j-2)))

def optimalDP(game):
    n = len(game)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for gap in range(1, n, 2):
        for i in range(n-gap):
            j = i+gap
            if i+1 == j: dp[i][j] = max(game[i], game[j])
            else: dp[i][j] = max(game[i] + min(dp[i+2][j], dp[i+1][j-1]),
                                    game[j] + min(dp[i][j-2], dp[i+1][j-1]))
    return dp[0][n-1]


#main:

game1 = [20, 5, 4, 6]
game2 = [2, 3, 15, 7]

res1 = optimal1(game1, 0, len(game1)-1, sum(game1))
res2 = optimal1(game2, 0, len(game1)-1, sum(game1))
res3 = optimal2(game1, 0, len(game1)-1)
res4 = optimal2(game2, 0, len(game1)-1)
res5 = optimalDP(game1)
res6 = optimalDP(game2)

print(res1, res3, res5)
print(res2, res4, res6)