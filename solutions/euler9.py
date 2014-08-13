#Special Pythagorean triplet https://projecteuler.net/problem=9
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