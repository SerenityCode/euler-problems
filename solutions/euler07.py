# 10001st prime https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from math import sqrt


def factorList(number):
    factors = []
    #ignore 1 as it isn't prime and skip even numbers
    for i in range(3, int(sqrt(number)) + 1, 2):
            if number % i == 0:
                factors.append(i)
                factors.append(number/i)
    return factors

primes = [2]
#Start at one as it is instantly incremented to 3
number = 1
while len(primes) < 10001:
    number += 2
    if len(factorList(number)) == 0:
        primes.append(number)

print primes[-1]