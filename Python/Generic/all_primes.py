n = int(input())
def sieve(n):
    primes = [True]*(n + 1)
    p = 2

    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n + 1, p):
                primes[i] = False

        p += 1

    for i in range(2, n + 1):
        if primes[i]:
            print(i)

sieve(n)
