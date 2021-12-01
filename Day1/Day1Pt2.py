from os import truncate

input = open("input.txt")

num1 = 0
num2 = 0
num3 = 0
num4 = 0
numIncreases = 0

current = int(input.readline())
num1 = num1 + current

current = int(input.readline())
num1 = num1 + current
num2 = num2 + current

current = int(input.readline())
num1 = num1 + current
num2 = num2 + current
num3 = num3 + current

for line in input:
    current = int(line)
    num2 = num2 + current
    num3 = num3 + current
    num4 = num4 + current

    if (num2 > num1):
        numIncreases = numIncreases + 1
    num1 = num2
    num2 = num3
    num3 = num4
    num4 = 0

print(numIncreases)