def even_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

x = int(input())
gen = even_generator(x)

for even in gen:
    print(even ,end=",")