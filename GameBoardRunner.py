from GameBoard import GameBoard

def main():
    spots = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]

    gb = GameBoard(spots)
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    n = 0


    for i in range(len(spots)):
        if(n % 2 == 0):
            spot = int(input("Player X: ")) - 1
            while(spots[spot] != 0 or spot < 0):
                spot = int(input("SPOT IS NOT AVAILABLE TRY AGAIN\nPlayer X: ")) - 1
            spots[spot] = 1
        else:
            spot = int(input("Player O: ")) - 1
            while(spots[spot] != 0 or spot < 0):
                spot = int(input("SPOT IS NOT AVAILABLE TRY AGAIN\nPlayer O: ")) - 1
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
    if(n == 9 and not gb.xWins(spots) and not gb.oWins(spots)):
        print("It's a tie!")
    # time.sleep(5)




if __name__ == "__main__":
    main()
