play_status = {
"p1" : [0,0,0,0,0,0,0,0,0],
"p2" : [0,0,0,0,0,0,0,0,0]
}
def play(player,block):
    if [play_status["p1"][block-1],play_status["p2"][block-1]] == [0,0]: # avoids repetitive action
        play_status[player][block-1] = 1
        return play_status # new game status
    else:
        print("Now allowed!") # block is full


