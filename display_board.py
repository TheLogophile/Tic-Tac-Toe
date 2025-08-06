def display(status):
    p1d = [" X " if i else 0 for i in status["p1"]]
    p2d = [" O " if i else 0 for i in status["p2"]]
    v="Here is the Board: "
    for i in range(9): 
        if i%3 == 0:
            v = v + '\n'
        if p1d[i]:
            v = v + p1d[i]
        elif p2d[i]:
            v = v + p2d[i]
        else:
            v = v + " _ "
    print(v)


play_status = {
"p1" : [0,0,0,0,0,0,0,0,0],
"p2" : [0,0,0,0,0,0,0,0,0]
}
display(play_status)


