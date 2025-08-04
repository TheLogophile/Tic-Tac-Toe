from play_game import play
from display_board import display
from winner_check import winner

print("Welcome! We use numbers to refer board positions. Let's go!")

while True:
    p1c = int(input("Player 1 - draw an X : "))
    move = play("p1", p1c)
    display(move)
    if winner(move["p1"]):
        print("X WINS!")
        break
    p2c = int(input("Player 2 - draw an O : "))
    move = play("p2", p2c)
    display(move)
    if winner(move["p2"]):
        print("O WINS!")
        break


