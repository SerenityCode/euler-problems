# Maximum path sum II https://projecteuler.net/problem=67
# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt
# a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible
# to try every route to solve this problem, as there are 2^99 altogether!
# If you could check one trillion (1012) routes every second it would take over
# twenty billion years to check them all. There is an efficient algorithm to
# solve it. ;o)

triangle = open('triangle.txt', mode='r')
maximum = 0
triangle_list = []

for line in triangle:
    numbers = line.split(" ")
    numbers = map(int, numbers)
    triangle_list.append(numbers)
triangle.close()

def calculateRowSum(rows, index):
    for i in range(0, len(rows[index])):
        left = rows[index+1][i]
        right = rows[index+1][i+1]
        if left > right:
            rows[index][i] += left
        else:
            rows[index][i] += right
    if index != 0:
        calculateRowSum(rows, index-1)
    return rows

print calculateRowSum(triangle_list, len(triangle_list)-2)[0]