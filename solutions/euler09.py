#Special Pythagorean triplet https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a, b, c = 0, 0, 0
for i in range(1 , 1001):
    for j in range(i + 1, 1001):
        root = (i**2 + j**2)**(0.5)
        if i + j + root == 1000:
            a = i
            b = j
            c = root


print a
print b
print c
print a*b*c