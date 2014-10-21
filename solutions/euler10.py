# Summation of primes https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from math import sqrt


def factorList(number):
    factors = []
    #ignore 1 as it isn't prime and skip even numbers
    for i in range(3, int(sqrt(number)) + 1, 2):
            if number % i == 0:
                factors.append(i)
                factors.append(number/i)
                break
    return factors

primes = [2]
for i in range(3, 2000000, 2):
    if len(factorList(i)) == 0:
        primes.append(i)
print sum(primes)