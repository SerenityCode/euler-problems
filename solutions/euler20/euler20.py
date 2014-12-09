# Factorial digit sum https://projecteuler.net/problem=20
# n! means n x (n - 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

result = 100
digitSum = 0

for i in range (99, 0, -1):
    result *= i

#split the digits
result = str(result)

for c in result:
    digitSum += int(c)

print digitSum