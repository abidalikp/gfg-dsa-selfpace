def frequency(arr):
    d = dict()
    for x in arr:
        if x in d: d[x] += 1
        else: d[x] = 1
    for k, v in d.items():
        print(k, v)

def frequencySorted(arr):
    n = len(arr)
    freq = 1
    for i in range(1, n):
        if arr[i] == arr[i-1]: freq += 1
        else:
            print(arr[i-1], " ", freq)
            freq = 1
    print(arr[-1], " ", freq)

#main:

l = [10, 20, 30, 20, 30, 10, 20, 30, 40]

frequencySorted(sorted(l))
