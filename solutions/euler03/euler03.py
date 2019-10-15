# Largest prime factor https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def is_prime(number):
    """Tests if a number is prime"""
    #ignore 1 as it isn't prime and skip even numbers
    for i in range(3, int(sqrt(number)) + 2):
        if number % i == 0:
            return False
    return True

def factorList(number):
    """Returns all odd factors above 1 for a given number"""
    factors = []
    #ignore 1 as it isn't prime and skip even numbers
    for i in range(3, int(sqrt(number)) + 2):
        # If we have the first of number of the two factors we can work out 
        # the other i.e. if the number is 10 and we have 2 we can work out 5 is
        # the other number for 2 x 5 to make 10
        # this saves looping past the sqrt of the number
        if number % i == 0:
            factors.append(i)
            factors.append(number/i)
    return factors

# First get the odd factors for 600851475143
factors = factorList(600851475143)

primes = []
# Loop through the odd factors of the large number and check if they are prime
for factor in factors:
    if is_prime(factor):
        primes.append(factor)

print(f"The largest prime is {max(primes)}")
