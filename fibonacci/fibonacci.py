def fib_a(n):
    if n in (1,2,3):
        return(1)
    else:
        return(fib_a(n-3) + fib_a(n-2) + fib_a(n-1))

results_a = []
for i in range(1,30):
    results.append(fib_a(i))
print(results)

def fib_b(n, known = {1:1, 2:1, 3:1}):
    if n not in known:
        known[n] = fib_b(n-3, known) + fib_b(n-2, known) + fib_b(n-1, known)
    return(known[n])

results_b = []
for i in range(1,10000):
    results_b.append(fib_b(i))

print(results_b[-10:])
print(fib_b(1000))

def fib_c(n):
    a, b, c = 1, 1, 1
    if n <= 3:
        return(1)
    else:
        for i in range(n-3):
            a, b, c = b, c, a + b + c
    return(c)

results_c = []
for i in range(1,10000):
    results_c.append(fib_c(i))
print(results_c[-10:])
print(fib_c(10000))
