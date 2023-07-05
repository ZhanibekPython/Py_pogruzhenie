
fib = lambda n,a=0,b=1: a if n<=0 else fib(n-1,b,a+b)
print(fib(11))


def fibonacci(num):
    a, b = 0, 1
    while a < num:
        yield a
        a, b = b, a + b


for i in fibonacci(15):
    print(i)

def fibo(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    yield b



print(*fibo(10))
