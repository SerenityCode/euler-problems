# Counting Sundays https://projecteuler.net/problem=19
# You are given the following information, but you may prefer to do some
# research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century
#  (1 Jan 1901 to 31 Dec 2000)?


# I've already worked out that the first day in 1901 is a Tuesday so we
# will start there
startingDay = 1 # 0 = Monday 6 = Sunday
days = 0 # Sundays on the first of the month
sunDays = {}
sunLeapDays = {}

for i in range(1901, 2001):
    # reset values for each year
    sundayDate = 7 - startingDay
    leap = False
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        leap = True
    if startingDay < 6:
        startingDay += 1
    else:
        startingDay = 0
    if leap:
        if startingDay < 6:
            startingDay += 1
        else:
            startingDay = 0

    # potential for 53 sundays in a year
    for j in range(0, 53):
        if leap:
            sunLeapDays[sundayDate] = sunLeapDays.get(sundayDate, 0 ) + 1
        else:
            sunDays[sundayDate] = sunDays.get(sundayDate, 0 ) + 1
        sundayDate += 7

validDays = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
validLeapDays = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]

for day in validDays:
    days += sunDays[day]
for day in validLeapDays:
    days += sunLeapDays[day]

print days
