# Names scores https://projecteuler.net/problem=22

# Using names.txt (see p022_names.txt), a 46K text file
# containing over five-thousand first names, begin by sorting it into
#  alphabetical order. Then working out the alphabetical value for each name,
#  multiply this value by its alphabetical position in the list to obtain a
# name score.

# For example, when the list is sorted into alphabetical order, COLIN,
#  which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?

file = open('p022_names.txt', mode='r')
names = file.read().split(',')
file.close()
names = sorted(names)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_dict = {}
for i in range(0, len(alphabet)):
    alphabet_dict[alphabet[i]] = i+1

total = 0
for i in range(0, len(names)):
    cSum = 0
    for c in names[i][1:-1]:
        cSum += alphabet_dict[c]
    total += cSum * (i + 1)

print total