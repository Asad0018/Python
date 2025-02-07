# Returns the name length:
def name_length(name):
    return len(name)

# Prints stars:
def stars(n):
    for x in range(n):
        print('*', end = '')

# returns a list of 1 to n:
def natural_numbers(n):
    l = []
    for x in range(1, n + 1):
        l.append(x)
    return l

# Factorial:
def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

# Fibonacci:
def fib(n):
    if n < 3:
        return n - 1
    return fib(n - 1) + fib(n - 2)

# Fibonacci sequence:
def fib_list(n):
    l = natural_numbers(n)
    return list(map(fib, l))

# Returns True if the number is prime:
def prime_check(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

# B.M.M :
def bmm(n1, n2):
    for x in range(n1, 0, -1):
        if n1 % x == 0 and n2 % x == 0:
            return x
        
# Print thr Multiplication table (heigh = width):
def mt(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end = '\t')
        print()

# The +++ shape:
def pluses(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print('+', end = ' ')
        print()

# Minimum:
def min(*args):
    iMin = 0
    for x in range(len(args)):
        if args[x] < args[iMin]:
            iMin = x
    return args[iMin]

# Maximum:
def max(*args):
    iMax = 0
    for x in range(len(args)):
        if args[x] > args[iMax]:
            iMax = x
    return args[iMax]

# Sort:
def sort(*args):
    l1 = list(args)
    l2 = []
    while l1:
        iMin = 0
        for i in range(len(l1)):
            if l1[i] < l1[iMin]:
                iMin = i
        l2.append(l1[iMin])
        del l1[iMin]
    return l2

# Average:
def avg(*args):
    sum = 0
    for x in range(len(args)):
        sum += args[x]
    return sum / len(args)

# Reverse string:
def reverse(s1):
    s2 = ''
    for x in range(len(s1)):
        s2 += s1[len(s1) - 1 - x]
    return s2

# The best and worse students:
def scores(**kwargs):
    names = []
    scores = []
    for name, score in kwargs.items():
        names.append(name)
        scores.append(score)
    iMin = 0
    iMax = 0
    for x in range(len(scores)):
        if scores[x] < scores[iMin]:
            iMin = x
        if scores[x] > scores[iMax]:
            iMax = x
    return {"The best" : names[iMax], "The worst" : names[iMin]}

# x^y :
def power(x, y):
    if y == 1:
        return x
    return x * power(x, y - 1)

    
