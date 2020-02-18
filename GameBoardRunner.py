from GameBoard import GameBoard

def main():
    spots = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]

    gb = GameBoard(spots)
    print(gb)
    n = 0
    for i in range(len(spots)):
        if(n % 2 == 0):
            spot = int(input("Player X: "))
            while(spots[spot] != 0):
                spot = int(input("SPOT IS ALREADY TAKEN TRY AGAIN\nPlayer X: "))
            spots[spot] = 1
        else:
            spot = int(input("Player O: "))
            while(spots[spot] != 0):
                spot = int(input("SPOT IS ALREADY TAKEN TRY AGAIN\nPlayer O: "))
            spots[spot] = 2
        n += 1
        gb = GameBoard(spots)
        print(gb)
        if(gb.xWins(spots)):
            print("Player X Wins!")
            break
        elif(gb.oWins(spots)):
            print("Player O Wins!")
            break
    if(n == 9):
        print("It's a tie!")
if __name__ == "__main__":
    main()
