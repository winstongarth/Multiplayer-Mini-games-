def printBoard(s, dic):
   if 2 < s < 11:
       for i in range(0, s**2-1, s):
            for ii in range(i, i+s-1):
                if dic[str(ii)] == "X" or dic[str(ii)] == "O":
                    print(" "+dic[str(ii)], end=' ') 
                elif ii > 9:
                    print(dic[str(ii)], end=' ')
                else:
                    print(" "+dic[str(ii)], end=' ')
            if dic[str(i+s-1)] == "X" or dic[str(i+s-1)] == "O":
                print(" "+dic[str(i+s-1)], end='') 
            elif (i+s-1) > 9:
                print(dic[str(i+s-1)], end = '') 
            else:
                print(" "+dic[str(i+s-1)], end = '') 
            print('')

def checkwin(turn, choose, dic, s):
    #vertical
    for i in range(s):
        found = True
        for col in range(i, s**2, s):
            if dic[str(col)] != turn:
                found = False
        if found:
            return True
    #horizontal
    for row in range(s):
        found = True
        for col in range(s):
            if dic[str(col+(row*s))] != turn:
                found = False
        if found:
            return True
    #diagonal tr to bl
    found = True
    for i in range(s-1, s**2-s+1, s-1):
        if dic[str(i)] != turn:
            found = False
    if found:
        return True
    #diagonal tl to br
    found = True
    for i in range(0, s**2, s+1):
        if dic[str(i)] != turn:
            found = False
    if found:
        return True
def checktie(dic):
    count = 0
    for i in range(len(dic)):
        if dic[str(i)].isalpha == True:
            count += 1
    if count == s**2:
        return True
        exit()
  
def main():
    global turn, choose, dic, s
    step = 0
    while True:
        step +=1
        if turn == "X":
            choose = input("X--> ")
            dic[choose] = "X"
            printBoard(s, dic)
        if turn == "O":
            choose = input("O--> ")
            dic[choose] = "O"
            printBoard(s, dic)
        
        if checkwin(turn, choose, dic, s):
            print(f'Winner: {turn}')
            break
        if step == s**2:
            print("Winner: None")
            break

        turn = "O" if turn == "X" else "X"

s = int(input("Size--> "))
dic = {}
turn = "X"
choose = 0

for i in range(s**2):
    dic.update({f'{i}': str(i)}) 
printBoard(s, dic)
main()
