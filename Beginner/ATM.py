withdrawlAmount, balance = input().split()
withdrawlAmount = int(withdrawlAmount)
balance = float(balance)

# print(withdrawlAmount)
# print(balance)

if (withdrawlAmount + 0.5 < balance) and (withdrawlAmount % 5 == 0):
    balance -= withdrawlAmount
    balance -= .5

print("%0.2f" % balance)
