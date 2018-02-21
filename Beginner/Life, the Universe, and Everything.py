# while True:
#     x = int(input())
#     if x == 42:
#         break
#     print(x)

i = 0
a = 0
array = []
while i < 1000:
# Randomly assuming the number of input will be 1000
    array.append(int(input()))
    if array[i] == 42:
        a = i
        i = 0
        break
    i += 1

while i < a:
    print(array[i])
    i += 1
