lines = int(input())
array = []

for _ in range(lines):
    array.append(int(input()))

# # Bubble sort
# for _ in range(lines):
#     for i in range(lines - 1):
#         if array[i] > array[i + 1]: array[i], array[i + 1] = array[i + 1], array[i]
array.sort()

# This takes more time
# for x in range(lines): print(array[x])
# compared to this:
for x in array: print(x)
