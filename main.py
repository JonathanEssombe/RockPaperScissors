import random

computer_choice = ['rock', 'paper', 'scissors']
playerscore = 0
computerscore = 0


def player_input(myinput, playerscore, computerscore):
    computer = random.choice(computer_choice)
    if myinput == 'rock':
        print('Computer input:', computer)
        if computer == computer_choice[0]:
            return (
            F'Its a Tie! \nComputerscore: {computerscore} \nPlayerscore: {playerscore}', playerscore, computerscore)
        if computer == computer_choice[1]:
            computerscore += 1
            return (F'Computer Wins! \nComputer score: {computerscore} \nPlayer score: {playerscore}', playerscore,
                    computerscore)
        if computer == computer_choice[2]:
            playerscore += 1
            return (
            F'Player Wins! \nComputer score: {computerscore} \nPlayer score: {playerscore}', playerscore, computerscore)
    if myinput == 'paper':
        print('Computer input:', computer)
        if computer == computer_choice[0]:
            playerscore += 1
            return (
            F'Player Wins! \nComputer score: {computerscore} \nPlayer score: {playerscore}', playerscore, computerscore)
        if computer == computer_choice[1]:
            return (
            F'Its a Tie! \nComputerscore: {computerscore} \nPlayerscore: {playerscore}', playerscore, computerscore)
        if computer == computer_choice[2]:
            computerscore += 1
            return (F'Computer Wins! \nComputer score: {computerscore} \nPlayer score: {playerscore}', playerscore,
                    computerscore)
    if myinput == 'scissors':
        print('Computer input:', computer)
        if computer == computer_choice[0]:
            computerscore += 1
            return (F'Computer Wins! \nComputer score: {computerscore} \nPlayer score: {playerscore}', playerscore,
                    computerscore)
        if computer == computer_choice[1]:
            playerscore += 1
            return (
            F'Player Wins! \nComputer score: {computerscore} \nPlayer score: {playerscore}', playerscore, computerscore)
        if computer == computer_choice[2]:
            return (
            F'Its a Tie! \nComputerscore: {computerscore} \nPlayerscore: {playerscore}', playerscore, computerscore)
    return ("please enter 'rock' 'paper' or 'scissors'!", playerscore, computerscore)


print(
    "PLAYER VS COMPUTER ROCK PAPER SCISSORS! \nRules: Enter 'rock', 'paper' or 'scissors' \n----------------------------")
while True:
    myinput = input('Player input: ')
    result, playerscore, computerscore = player_input(myinput, playerscore, computerscore)
    print(result, '\n ----------------------------')





