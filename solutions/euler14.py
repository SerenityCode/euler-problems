# Longest Collatz sequence https://projecteuler.net/problem=14
def n2(n, chain):
    if n == 1:
        return chain
    chain += 1
    if n % 2 == 0:
        return n2(n/2, chain)
    return n3(n, chain)


def n3(n, chain):
    if n == 1:
        return chain
    chain += 1
    return n2((n*3+1), chain)

chain = 0
largest_chain = 0
largest = 0
for i in range(1, 1000000):
    chain = n2(i, chain)
    if chain > largest_chain:
        largest_chain = chain
        largest = i
    chain = 0

print largest
