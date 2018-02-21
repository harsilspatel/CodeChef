lines, number = input().split()
lines = int(lines)
number = int(number)

# i = 0
# divisibleNumbers = 0
# array = []
# while i < lines:
# # As i = 0, the number of times the while loop will run is equal to 'lines'
#     array.append(int(input()))
#
#     if array[i] % number == 0:
#         divisibleNumbers += 1
#
#     i += 1
#
# print(divisibleNumbers)


i = 0
divisibleNumbers = 0
temporary = 0
array = []
while i < lines:
    temporary = int(input())
    if temporary % number == 0:
        divisibleNumbers += 1

    i += 1

print(divisibleNumbers)
