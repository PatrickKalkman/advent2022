# (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won)


# X for Rock, 
# Y for Paper, 
# Z for Scissors

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
        score = score + 3 + 1
    elif we == 'Y' and them == 'B':
        score = score + 3 + 2
    elif we == 'Z' and them == 'C':
        score = score + 3 + 3
    elif we == 'X' and them == 'B':
        score = score + 0 + 1
    elif we == 'X' and them == 'C':
        score = score + 6 + 1
    elif we == 'Y' and them == 'A':
        score = score + 6 + 2
    elif we == 'Y' and them == 'C':
        score = score + 0 + 2
    elif we == 'Z' and them == 'A':
        score = score + 0 + 3
    elif we == 'Z' and them == 'B':
        score = score + 6 + 3

print(score)
