def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

x = int(input())
gen = square_generator(x)

for value in gen:
    print(value)