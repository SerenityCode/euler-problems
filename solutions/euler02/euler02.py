# Even Fibonacci numbers https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...#
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

sequence = [1, 2]
sum = 0

while sequence[-1] < 4000000:
    if sequence[-1] % 2 == 0:
        sum += sequence[-1]
    sequence.append(sequence[-1]+sequence[-2])

print sum