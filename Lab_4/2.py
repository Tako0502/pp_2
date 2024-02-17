def squares_generator(N):
    for i in range(N):
        yield i ** 2

N = 10
for square in squares_generator(N):
    print(square)
 #-------------------------Tasks---------------------------
def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

even_numbers = even_numbers_generator(n)
for i in even_numbers:
    print(i)

 #-------------------------Tasks---------------------------


def divisible_by_3_and_4_generator(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

start = 0
end = 20
for num in divisible_by_3_and_4_generator(start, end):
    print(num)


 #-------------------------Tasks---------------------------
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = 1, 5
for square in squares(a, b):
    print(square)
 #-------------------------Tasks---------------------------


def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
for num in countdown_generator(n):
    print(num)


