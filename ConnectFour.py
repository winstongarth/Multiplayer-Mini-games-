def createBoard(r , c):
    if 'n' == input('Standard game? (y/n): '):
        r, c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    return [['·'] * c for i in range(r)]

def printBoard(board):
    r, c = len(board), len(board[0])
    spaces = 1
    if r>9 or c>9: spaces = 2 #bigBoard
    x = ''
    for row in range(r-1,-1, -1):
        x += f'{row:>{spaces}}'
        ss = ' '
        if spaces==2: ss = '  '
        for col in range(c):
            x += ss+board[row][col]
        x += ' \n'
    x += ' ' + ' '*spaces
    for col in range(c): x += f'{col:>{spaces}}'+' '
    print(x)

def makeMove(board, player, col):
    r = len(board)
    for row in range(r):
        if board[row][col]!='·' and board[row+1][col]=='·':
            board[row+1][col] = player
            break
        elif board[row][col]=='·':
            board[row][col] = player
            break

def checkwin(r, c):
    countx = 0
    counto = 0
    revboard = []
    for i in range(len(board)):
        revboard.append(board[i][::-1])
    if player == "X":
        for i in board: # row
            for ii in i:
                if ii == "X":
                    countx += 1
                elif ii == "·" or ii == 'O':
                    countx = 0
                if countx == 4:
                    return True
            countx = 0
        countx = 0
        for i in range(c): # col
            for ii in range(r):
                if board[ii][i] == "X":
                    countx += 1
                elif board[ii][i] == "·" or board[ii][i] == "O":
                    countx = 0
                if countx == 4:
                    return True
            countx = 0
        countx = 0
        for i in range(c-3): #diagonal tl to br
            for ii in range(r-1, r-4, -1):
                x = i
                y = ii
                while y != -1 and x != c:
                    if board[y][x] == "X":
                        countx += 1
                    elif board[y][x] == "·" or board[y][x] == "O":
                        countx = 0
                    if countx == 4:
                        return True
                    x += 1
                    y -= 1
                countx = 0
        countx = 0

        for i in range(c-3): #diagonal tr to bl
            for ii in range(r-1, r-4, -1):
                x = i
                y = ii
                while y != -1 and x != c:
                    if revboard[y][x] == "X":
                        countx += 1
                    elif revboard[y][x] == "·" or revboard[y][x] == "O":
                        countx = 0
                    if countx == 4:
                        return True
                    x += 1
                    y -= 1
                countx = 0
        
    if player == "O":
        for i in board: # row
            for ii in i:
                if ii == "O":
                    counto+= 1
                elif ii == "·" or ii == "X":
                    counto = 0
                if counto == 4:
                    return True
            counto = 0
        counto = 0
        for i in range(c): # col
            for ii in range(r):
                if board[ii][i] == "O":
                    counto += 1
                elif board[ii][i] == "·" or board[ii][i] == "X":
                    counto = 0
                if counto == 4:
                    return True
            counto = 0
        counto = 0
        for i in range(c-3): #diagonal tl to br
            for ii in range(r-1, r-4, -1):
                x = i
                y = ii
                while y != -1 and x != c:
                    if board[y][x] == "O":
                        counto += 1
                    elif board[y][x] == "·" or board[y][x] == "X":
                        counto = 0
                    if counto == 4:
                        return True
                    x += 1
                    y -= 1
                counto = 0
        counto = 0

        for i in range(c-3): #diagonal tr to bl
            for ii in range(r-1, r-4, -1):
                x = i
                y = ii
                while y != -1 and x != c:
                    if revboard[y][x] == "O":
                        counto += 1
                    elif revboard[y][x] == "·" or revboard[y][x] == "X":
                        counto = 0
                    if counto == 4:
                        return True
                    x += 1
                    y -= 1
                counto = 0
        counto = 0
        
    else:
        return False
               
r, c = 6, 7           
board = createBoard(r , c)
printBoard(board)
player = 'X'
steps = 0
while True:
    r = len(board)
    c = len(board[0])
    move = input( 'player'+player+' (col #): ')
    if move == 'e': break
    if board[r-1][int(move)] != "·":
        printBoard(board)
        continue
    steps += 1
    makeMove(board, player, int(move))
    printBoard(board)
    #print(board)
    if checkwin(r, c):
        print(f'Player {player} has won!')
        break
    if steps == r*c:
        print("Draw!")
        break
    if player == 'X': player = 'O'
    else: player = 'X'
print('bye')
