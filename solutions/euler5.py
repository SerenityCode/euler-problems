# Smallest multiple https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

n = 20

while True:
    worked = False
    for i in range(20, 0, -1):
        if n % i != 0:
            break
        if i == 1:
            worked = True
    if worked:
        break
    n += 20

print n