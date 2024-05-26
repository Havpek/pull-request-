import itertools as its
def fizz_buzz(n):
    fizzes = its.cycle([""] * 2 + ["Fizz"])
    buzzes = its.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, its.count(1)))
    for i in its.islice(result, n):
        print(i)
print(fizz_buzz(10))