# ############ yield and generators #############
# originally created by Michael Kennedy (@mkennedy)
# check out his python podcase talkpython.fm!
#


# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

# TODO: Check out the "6: TODO" tab below
# TODO: Show the red squiqqly lines in Project window.  Discuss Project window.  Toggle options & explain.  Show members & Structure tab.  Collapsing window.
# TODO: Show print() problem. Switch interpreters
# TODO: Demo 1) Basic debugging (breakpoints and stepping through) 2) TODO items
# TODO: Basic editor stuff, such as line numbers.

def classic_fibonacci(limit):
    nums = []
    current, nxt = 0, 1

    while current < limit:
        current, nxt = nxt, nxt + current
        nums.append(current)

    return nums


# fib via generators
def generator_fib():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        yield current


# generators support composition:
def even_fibonacci():
    for n in generator_fib():
        if n % 2 == 0:
            yield n


# consume both generators as a pipeline here
def composed_generators():
    for e in even_fibonacci():
        if e % 3 == 0:
            yield e


if __name__ == '__main__':

    print("Classic")
    for m in classic_fibonacci(100):
        print(m, end=', ')
    print()
    print(classic_fibonacci(10))
    print(generator_fib())

    print("generator")
    for m in generator_fib():
        print(m, end=', ')
        if m > 100:
            break
    print()

    print("composed")
    for m in composed_generators():
        print(m, end=', ')
        if m > 1000000:
            break
    print()
