lines = int(input())
playerOne = 0
increaseOne = 0
playerTwo = 0
increaseTwo = 0
leadingPlayer = 1
difference = 0

for _ in range(lines):
    increaseOne, increaseTwo = map(int, input().split())
    playerOne, playerTwo = playerOne + increaseOne, playerTwo + increaseTwo

    if abs(playerOne - playerTwo) > difference:
        difference = abs(playerOne - playerTwo)
        if playerOne > playerTwo: leadingPlayer = 1
        else: leadingPlayer = 2

print(leadingPlayer, difference)
