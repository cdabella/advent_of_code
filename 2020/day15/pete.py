input = [11,0,1,10,5,19]

#input = [0,3,6]

game = {}
turn = 0



for number in input:
    if turn > 0:
        game.update({last:turn})
    turn = turn + 1
    last = number


playing = True

while playing:
    turn = turn + 1
    if last not in game:
        number = 0
        game.update({last:turn-1})
    else:
        number = (turn - 1) - game[last]
        game.update({last:turn-1})
    last = number
    if turn == 30000000:
        print(number)
        break
