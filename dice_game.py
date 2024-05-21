
import random

# random number generator
def roll():
    min = 1
    max = 6
    return random.randint(min, max)


# ask how many players are there
while True :
    players = input("How many players are there?(max is 4 players) : ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
           print("Please enter a number less than or equal to 4")
    else:
        print("Please enter a number")

# print(players)

maxScore = 10
playersScores = [0 for _ in range((players))]
# print(playersScores)

while max(playersScores) < maxScore:
    for idx in range(players):
        print("\n player ",idx + 1,"turn has started\n")
        currentScore = 0
        while True:
            wantToRoll = input("would you like to roll ?(y or n)")
            if wantToRoll.lower() == "y":
                value = roll()
                if value == 1:
                    print("you rolled a 1, your turn is over")
                    currentScore = 0
                    break
                else:
                    print("you rolled a ",value)
                    currentScore += value
                print("your current score is ",currentScore)
            elif wantToRoll.lower() == "n":
                break
            else:
                print("please enter y or n")
        playersScores[idx]  +=currentScore
        print("player ",idx + 1," score is ",playersScores[idx])
maxScore = max(playersScores)
winIdx = playersScores.index(maxScore)
print("player ",winIdx + 1," won the game")





