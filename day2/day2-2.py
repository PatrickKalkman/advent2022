# (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win. Good luck!"

# A for Rock, 
# B for Paper, and 
# C for Scissors.

game_file = open('./input.txt', 'r')
games = game_file.readlines()
game_file.close()
score = 0

for game in games:
    set = game.strip().split(' ')
    them = set[0].upper()
    we = set[1].upper()
    print(them + " " + we)
    if we == 'X' and them == 'A':
        # we choose scissors
        score = score + 0 + 3
    elif we == 'Y' and them == 'B':
        # we choose paper
        score = score + 3 + 2
    elif we == 'Z' and them == 'C':
        # we choose rock
        score = score + 6 + 1
    elif we == 'X' and them == 'B':
        # we choose rock
        score = score + 0 + 1
    elif we == 'X' and them == 'C':
        # we choose paper
        score = score + 0 + 2
    elif we == 'Y' and them == 'A':
        # we choose rock
        score = score + 3 + 1
    elif we == 'Y' and them == 'C':
        # we choose scissors
        score = score + 3 + 3
    elif we == 'Z' and them == 'A':
        # we choose paper
        score = score + 6 + 2
    elif we == 'Z' and them == 'B':
        # we choose scissors
        score = score + 6 + 3

print(score)
