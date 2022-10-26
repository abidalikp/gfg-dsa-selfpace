def reverseWords(string):
    stack = string.split()
    ans = ''
    n = len(stack)
    for _ in range(n):
        ans += stack.pop() + ' '
    return ans

#main:

strings = []
strings.append('welcome to gfg')
strings.append('i love coding')
strings.append('awesome')


for string in strings:
    ans = reverseWords(string)
    print(ans)