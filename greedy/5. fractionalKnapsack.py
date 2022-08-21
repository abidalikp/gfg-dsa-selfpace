def maxValue(weights, values, capacity):
    arr = []
    for x, y in zip(weights, values):
        arr.append((x, y))
    arr.sort(key = lambda k: k[1]/k[0], reverse= True)
    ans = 0
    bal = capacity
    for w, v in arr:
        if w < bal:
            bal -= w
            ans += v
        else:
            ans += (bal/w*v)
            return ans
    return ans

#main:

weights = [50, 20, 30]
values = [600, 500, 400]
capacity = 70

res = maxValue(weights, values, capacity)

print(res)