# Amicable Numbers https://projecteuler.net/problem=21

# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a == b, then a and b are an
# amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
#  55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
#  71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

divisorSums = {}
amicablepairs = []
def sumDivisors(number):
    divisors = []
    for j in range(1, number):
        if number % j == 0:
            divisors.append(j)
    return sum(divisors)

#plan is to calculate all divisor sums first and then check for pairs
for i in range(1, 10000):
    divisorSums[i] = sumDivisors(i)

for key,value in divisorSums.items():
    try:
        if value != key:
            if divisorSums[value] == key:
                amicablepairs.append(key)
    except KeyError:
        pass

print sum(amicablepairs)
