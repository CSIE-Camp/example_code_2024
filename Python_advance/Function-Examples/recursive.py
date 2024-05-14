def Fibonacci(n):
    if n < 2:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(10))

# https://zh.wikipedia.org/zh-tw/費波那契數