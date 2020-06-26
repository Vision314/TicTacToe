class GameBoard:

    def __init__(self, spots):
        self.spots = spots
        self.board = [["" for i in range(3)] for j in range(3)]

        self.populate(spots)

    def populate(self, init):
        n = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(init[n] == 0):
                    self.board[i][j] = "   ";
                elif(init[n] == 1):
                    self.board[i][j] = " X ";
                elif(init[n] == 2):
                    self.board[i][j] = " O ";
                n += 1

    def xWins(self, spots):
        if((spots[0] == 1 and spots[1] == 1 and spots[2] == 1) or
           (spots[3] == 1 and spots[4] == 1 and spots[5] == 1) or
           (spots[6] == 1 and spots[7] == 1 and spots[8] == 1) or
           (spots[0] == 1 and spots[3] == 1 and spots[6] == 1) or
           (spots[1] == 1 and spots[4] == 1 and spots[7] == 1) or
           (spots[2] == 1 and spots[5] == 1 and spots[8] == 1) or
           (spots[0] == 1 and spots[4] == 1 and spots[8] == 1) or
           (spots[6] == 1 and spots[4] == 1 and spots[2] == 1)):
            return True
        else:
            return False
    def oWins(self, spots):
        if((spots[0] == 2 and spots[1] == 2 and spots[2] == 2) or
           (spots[3] == 2 and spots[4] == 2 and spots[5] == 2) or
           (spots[6] == 2 and spots[7] == 2 and spots[8] == 2) or
           (spots[0] == 2 and spots[3] == 2 and spots[6] == 2) or
           (spots[1] == 2 and spots[4] == 2 and spots[7] == 2) or
           (spots[2] == 2 and spots[5] == 2 and spots[8] == 2) or
           (spots[0] == 2 and spots[4] == 2 and spots[8] == 2) or
           (spots[6] == 2 and spots[4] == 2 and spots[2] == 2)):
            return True
        else:
            return False

    def __str__(self):
        str = "";
        j = 0
        for i in range(len(self.board)):
            if(j == 1 or j == 2):
                str += "\n-----------\t-----------\n"
            str += self.board[i][0] + "|" + self.board[i][1] + "|" + self.board[i][2]
            if(i == 0):
                str += "\t 1 | 2 | 3 "
            elif(i == 1):
                str += "\t 4 | 5 | 6 "
            elif(i == 2):
                str += "\t 7 | 8 | 9 "
            j += 1
        return str
