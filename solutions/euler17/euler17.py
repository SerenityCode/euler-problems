# Number Letter Counts https://projecteuler.net/problem=17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


# I'm sure you could use a multiple dimension array here but lets keep it simple
unique = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
          'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
multipleTens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                'eighty', 'ninety']

def numToLetterCount(number):
    if number < 20:
        return len(unique[i-1])

    if number < 100:
        # split the number and return the word for each part
        split = str(number)
        if int(split[1]) > 0:
            return len(multipleTens[int(split[0])-2]) \
                   + len(unique[int(split[1])-1])
        else:
            return len(multipleTens[int(split[0])-2])

    if number < 1000:
        split = str(number)
        numString = unique[int(split[0])-1] + 'hundred'
        if int(split[1:]) > 0:
            numString += 'and'
        if int(split[1:]) > 0 and int(split[1:]) < 20:
            # use eleven, twelve etc rather than tenone, tentwo
            numString += unique[int(split[1:])-1]
        else:
            if int(split[1]) > 1:
                numString += multipleTens[int(split[1])-2]
            if int(split[2]) > 0:
                numString += unique[int(split[2])-1]
        return len(numString)

    # number is one thousand which is 11 characters
    return 11

count = 0
for i in range(1, 1001):
    count += numToLetterCount(i)

print count
