from os import truncate

input = open("input.txt")

last = int(input.readline())
numIncreases = 0

for line in input:
    current = int(line)
    if (current > last):
         numIncreases = numIncreases + 1
    last = current

print(numIncreases)