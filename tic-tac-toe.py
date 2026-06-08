#   | |    0R
#  -----   1R
#   | |    2R
#  -----   3R
#   | |    4R
#c 01234

def drawField(field):
    for row in range(5): #0,1,2,3,4
                         #0,.,1,.,2
        if row%2 == 0: #0,2,4
            practicalRow = int(row/2)
            for column in range(5): #0,1,2,3,4,
                                    #0,.,1,.,2
                if column%2 == 0: #0,2,4
                    practicalColumn = int(column/2)
                    if column != 4:
                        print(field[practicalColumn][practicalRow],end ="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|",end = "")
        else:
            print("-|-|-")
            
def checkWinner(field):
    #Rows
    for row in range(3):
        if field[0][row] == field[1][row] == field[2][row] != " ":
            return True
    #Columns
    for col in range(3):
        if field[col][0] == field[col][1] == field[col][2] != " ":
            return True
    #Diagonal 1
    if field[0][0] == field[1][1] == field[2][2] != " ":
        return True
    #Diagonal 2
    if field[2][0] == field[1][1] == field[0][2] != " ":
        return True
    return False
Player = 1
currentField = [[" "," "," "],[" "," "," "],[" "," "," ",]]
drawField(currentField)
moveCount = 0
while(True):
    print("Players Turn:",Player)
    MoveRow = int(input("Please enter the row\n"))
    MoveColumn = int(input("Please enter the column\n"))
    if Player == 1:
        #make move for Player 1
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            Player = 2
    else:
        #make move for Player 2
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            Player = 1
    drawField(currentField)
    
    #Winner check
    if checkWinner(currentField):
        print("="*30)
        print("GAME OVER")
        if Player == 1:
            Player = 2
        elif Player == 2:
            Player = 1
        print("Player",Player,"Wins!")
        print("="*30)
        break
    #Draw check
    if moveCount == 9:
        print("="*30)
        print("GAME OVER")
        print("It is a Draw!")
        print("="*30)
        break
