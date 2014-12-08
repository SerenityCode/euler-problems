# Maximum sum sum 1 https://projecteuler.net/problem=18
# By starting at the top of the triangle below and moving to adjacent numbers
#  on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:
# see triangle.txt
# NOTE: As there are only 16384 routes, it is possible to solve this problem by
#  trying every route. However, Problem 67, is the same challenge with a
# triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)

# I am doing this one and problem 67 at the same time which is why this has a
# triangle.txt added

triangle = open('triangle.txt', mode='r')
maximum = 0
triangle_list = []

#build a list of lists for each row of the triangle
for line in triangle:
    numbers = line.split(" ")
    numbers = map(int, numbers)
    triangle_list.append(numbers)
triangle.close()

# I unfortunately googled for the concept (not the code!) as
# I didn't want to brute force this solution and I believed there was
#  an algorithm to do it.
# Turns out the method is quite smart, by starting at the row 2nd to bottom you
# calculate the maximum value that the numbers in that row can be and replace
# them with those numbers so for example say the triangle is
#      1
#    2   3
#  4   5   6
# you would try 2 + 4 or 5 and 3 + 5 or 6 to see which produced the highest
# number and replace the 2 and 3 with the value so it becomes
#      1
#    7   9
#  4   5   6
# Then you try this again for every row above until you reach the top

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