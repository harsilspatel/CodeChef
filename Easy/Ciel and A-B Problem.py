inputA, inputB = map(int, input().split())
outputNumber = ""
differenceString = [int(x) for x in str(abs(inputA - inputB))]

if differenceString[0] == 1: differenceString[0] = 2
else: differenceString[0] = 1
for x in differenceString: outputNumber += str(x)
print(outputNumber)
