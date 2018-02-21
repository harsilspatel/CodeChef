coins = 0
exchange = 0

# while True:
#     coins = input()
#     if coins == "": break
#     coins = int(coins)

# Recursion!
def divideCoins(coins):
    exchange = divideCoins(int(coins/2)) + divideCoins(int(coins/3)) + divideCoins(int(coins/4))
    # exchange = diint(coins/2) + int(coins/3) + int(coins/4)
    if coins > exchange: return coins
    else: return exchange

while True:
    try:
        coins = int(input())
        print(divideCoins(coins))
    except EOFError:
        break
