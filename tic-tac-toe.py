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
drawField()
stops at 14:33
