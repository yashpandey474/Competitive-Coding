
def checkMember(n):
#Implement Your Code Here
    cache = {0: 0, 1: 1}

    if n == 0 or n == 1:
        return True

    def generate(term):
        if term in cache:
            return cache[term]

        cache[term] = generate(term - 1) + generate(term - 2)

        if cache[term] >= n:
            return cache[term]

        return generate(term + 1)

    return generate(2) == n
