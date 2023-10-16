def printBoard():
    if len(possibleboard) == 3:
        print("A      B      C")
        print(f'{" ".join(boarda[0])}  {" ".join(boardb[0])}  {" ".join(boardc[0])}')
        print(f'{" ".join(boarda[1])}  {" ".join(boardb[1])}  {" ".join(boardc[1])}')
        print(f'{" ".join(boarda[2])}  {" ".join(boardb[2])}  {" ".join(boardc[2])}')
    elif len(possibleboard) == 2 and boarda not in possibleboard:
        print("B      C")
        print(f'{" ".join(boardb[0])}  {" ".join(boardc[0])}')
        print(f'{" ".join(boardb[1])}  {" ".join(boardc[1])}')
        print(f'{" ".join(boardb[2])}  {" ".join(boardc[2])}')
    elif len(possibleboard) == 2 and boardb not in possibleboard:
        print("A      C")
        print(f'{" ".join(boarda[0])}  {" ".join(boardc[0])}')
        print(f'{" ".join(boarda[1])}  {" ".join(boardc[1])}')
        print(f'{" ".join(boarda[2])}  {" ".join(boardc[2])}')
    elif len(possibleboard) == 2 and boardc not in possibleboard:
        print("A      B")
        print(f'{" ".join(boarda[0])}  {" ".join(boardb[0])}')
        print(f'{" ".join(boarda[1])}  {" ".join(boardb[1])}')
        print(f'{" ".join(boarda[2])}  {" ".join(boardb[2])}')
    elif len(possibleboard) == 1 and boarda in possibleboard:
        print("A")
        print(f'{" ".join(boarda[0])}')
        print(f'{" ".join(boarda[1])}')
        print(f'{" ".join(boarda[2])}')
    elif len(possibleboard) == 1 and boardb in possibleboard:
        print("B")
        print(f'{" ".join(boardb[0])}')
        print(f'{" ".join(boardb[1])}')
        print(f'{" ".join(boardb[2])}')
    elif len(possibleboard) == 1 and boardc in possibleboard:
        print("C")
        print(f'{" ".join(boardc[0])}')
        print(f'{" ".join(boardc[1])}')
        print(f'{" ".join(boardc[2])}')

def checklegalmove(choose):
    if len(choose) != 2:
        return True
    if choose[0] != "A" and choose[0] != "B" and choose[0] != "C": 
        return True
    if boarda not in possibleboard:
        if choose[0] == "A":
            return True
    if boardb not in possibleboard:
        if choose[0] == "B":
            return True
    if boardc not in possibleboard:
        if choose[0] == "C":
            return True
    if choose[1] not in [str(i) for i in range(9)]:
        return True
    if choose[0] =="A":#overlap @boarda
        if 0 <= int(choose[1]) < 3:
            if boarda[0][int(choose[1])] == "X":
                return True
        elif 3 <= int(choose[1]) < 6:
            if boarda[1][int(choose[1])-3] == "X":
                return True
        elif 6 <= int(choose[1]) < 9:
            if boarda[2][int(choose[1])-6] == "X":
                return True
    if choose[0] =="B":#overlap @boardb
        if 0 <= int(choose[1]) < 3:
            if boardb[0][int(choose[1])] == "X":
                return True
        elif 3 <= int(choose[1]) < 6:
            if boardb[1][int(choose[1])-3] == "X":
                return True
        elif 6 <= int(choose[1]) < 9:
            if boardb[2][int(choose[1])-6] == "X":
                return True
    if choose[0] =="C": #overlap @boardc
        if 0 <= int(choose[1]) < 3:
            if boardc[0][int(choose[1])] == "X":
                return True
        elif 3 <= int(choose[1]) < 6:
            if boardc[1][int(choose[1])-3] == "X":
                return True
        elif 6 <= int(choose[1]) < 9:
            if boardc[2][int(choose[1])-6] == "X":
                return True
    
def checkboardadie(possibleboard, boarda):
    for i in boarda:#board a
        if i.count("X") == 3:
            possibleboard.remove(boarda)
            return boarda
    for i in range(3):
        if boarda[0][i] == boarda[1][i] == boarda[2][i]:
            possibleboard.remove(boarda)
            return boarda
    if boarda[0][0] == boarda[1][1] == boarda[2][2] or boarda[0][2] == boarda[1][1] == boarda[2][0]:
        possibleboard.remove(boarda)
        return boarda
    else:
        return boarda
def checkboardbdie(possibleboard, boardb):
    for i in boardb:#board b
        if i.count("X") == 3:
            possibleboard.remove(boardb)
            return boardb
    for i in range(3):
        if boardb[0][i] == boardb[1][i] == boardb[2][i]:
            possibleboard.remove(boardb)
            return boardb
    if boardb[0][0] == boardb[1][1] == boardb[2][2] or boardb[0][2] == boardb[1][1] == boardb[2][0]:
        possibleboard.remove(boardb)
        return boardb
    else:
        return boardb   
def checkboardcdie(possibleboard, boardc):
    for i in boardc:#board b
        if i.count("X") == 3:
            possibleboard.remove(boardc)
            return boardc
    for i in range(3):
        if boardc[0][i] == boardc[1][i] == boardc[2][i]:
            possibleboard.remove(boardc)
            return boardc
    if boardc[0][0] == boardc[1][1] == boardc[2][2] or boardc[0][2] == boardc[1][1] == boardc[2][0]:
        possibleboard.remove(boardc)
        return boardc
    else:
        return boardc      

def main():
    global turn, boarda, boardb, boardc, possibleboard
    while True:
        choose = input(f"Player {turn}: ")
        if checklegalmove(choose):
            print("Invalid move, please input again")
            continue
        if choose[0] == "A":
            if 0 <= int(choose[1]) < 3:
                boarda[0][int(choose[1])] = "X" 
            elif 3 <= int(choose[1]) < 6:
                boarda[1][int(choose[1])-3] = "X" 
            elif 6 <= int(choose[1]) < 9:
                boarda[2][int(choose[1])-6] = "X" 
        if choose[0] == "B":
            if 0 <= int(choose[1]) < 3:
                boardb[0][int(choose[1])] = "X" 
            elif 3 <= int(choose[1]) < 6:
                boardb[1][int(choose[1])-3] = "X" 
            elif 6 <= int(choose[1]) < 9:
                boardb[2][int(choose[1])-6] = "X" 
        if choose[0] == "C":
            if 0 <= int(choose[1]) < 3:
                boardc[0][int(choose[1])] = "X" 
            elif 3 <= int(choose[1]) < 6:
                boardc[1][int(choose[1])-3] = "X" 
            elif 6 <= int(choose[1]) < 9:
                boardc[2][int(choose[1])-6] = "X" 
        if boarda in possibleboard:
            checkboardadie(possibleboard, boarda)
        if boardb in possibleboard:
            checkboardbdie(possibleboard, boardb)
        if boardc in possibleboard:
            checkboardcdie(possibleboard, boardc)
        turn = 2 if turn == 1 else 1
        printBoard()  
        if possibleboard == []:
            print(f"Player {turn} wins game")
            exit()

turn = 1

boarda = [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
boardb = [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
boardc = [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
possibleboard = [boarda, boardb, boardc]
printBoard()
main()
