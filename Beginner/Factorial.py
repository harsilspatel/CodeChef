'''
lines = int(input())
temporary = 0
# numberOfTwos = 0
numberOfFives = 0
# numberOfTens = 0

for _ in range(lines):
    temporary = int(input())
    numberOfFives = 0

    for i in range(0, temporary + 1, 5):
        # print(i)
        # if i % 2 == 0:
        #     numberOfTwos =+ 1
        if i == 0: continue
        if i % 5 == 0: numberOfFives += 1

        # if i % 10 == 0:
        #     numberOfTens += 1

    print(numberOfFives)
'''

lines = int(input())
temporary = 0
i = 5
numberOfZeros = 0

for _ in range(lines):
    temporary = int(input())
    i = 5
    numberOfZeros = 0

    while i <= temporary:
        numberOfZeros += int(temporary/i)
        i *= 5

    print(numberOfZeros)
