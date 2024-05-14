def f(x):
    return x + 1

print(f(1))


def g(x, y):
    return (x**3) + y

print(g(1, 2))


def h(x = 10):
    return x + 1

print(h())


def i():
    return 10

print(i())


def j(x):
    return x + 10, x + 20

print(j(1))
a, b = j(1)
print(a, b)
