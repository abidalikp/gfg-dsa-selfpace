def fun1(n):
    if not n: return
    print(n)
    fun1(n-1)
    print(n)

def fun2(n):
    if not n: return
    fun2(n-1)
    print(n)
    fun2(n-1)

# main:

n = 7

fun1(n)
fun2(n)
