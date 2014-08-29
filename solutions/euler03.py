# Largest prime factor https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt


def factorList(number):
    factors = []
    #ignore 1 as it isn't prime and skip even numbers
    for i in range(3, int(sqrt(number)) + 2):
            if number % i == 0:
                factors.append(i)
                factors.append(number/i)
    return factors

factors = factorList(600851475143)
largest_prime = 0
for factor in factors:
    if len(factorList(factor)) == 0:
        if factor > largest_prime:
            largest_prime = factor

print largest_prime