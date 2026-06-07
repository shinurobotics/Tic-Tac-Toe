#   | |    0R
#  -----   1R
#   | |    2R
#  -----   3R
#   | |    4R
#c 01234

def drawField():
    for row in range(5):
        if row%2 == 0:
            for column in range(5):
                if column%2 == 0:
                    if column != 4:
                        print(" ",end = "")
                    else:
                        print(" ")
                else:
                    print("|",end = "")
        else:
            print("-----")
Player = 1
currentField = [[" "," "," "],[" "," "," "],[" "," "," ",]]
print(currentField)
while(True):
    print("Players Turn:",Player)
    MoveRow = int(input("Please enter the row\n"))
    MoveColumn = int(input("Please enter the column\n"))
    if Player == 1:
        #make move for Player 1
        currentField[MoveColumn][MoveRow] = "X"
        Player = 2
    else:
        #make move for Player 2
        currentField[MoveColumn][MoveRow] = "O"
        Player = 1
    print(currentField)
