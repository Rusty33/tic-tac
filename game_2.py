import random

board = [[0,0,0],[0,0,0],[0,0,0]]
turn = 1
game = True
go = True
#####################################################
def print_board():
    global board
    to_print = [""," 1 "," 2 "," 3 ","\n"]
    x = 0
    y = 0
    

    while y <= 2:
        
        if board[y][x] == 0:
            to_print.append("   ")

        if board[y][x] == 1:
            to_print.append(" X ")

        if board[y][x] == 2:
            to_print.append(" O ")

        if x == 2:
            x = -1
            y += 1
            to_print.append("\n")
            
            
        x += 1

    to_print.append("tic_tac_toe")
    to_print.append("\n")
    to_print.append("  player%s  " % (turn)) 
    for p in to_print:
        print(p,end="|")
#####################################################
def play():
    global turn
    print("\n")
    
    x = int(input("|Please pick a row|"))
    x -= 1
    y = int(input("|And how far down |"))
    y -= 1
    
    if x >= 3 or y >= 3:
        print("|Please choose a blank space|")
    else:
        if board[y][x] != 0:
            print("|Please choose a blank space|")
            play()
        else:
            board[y][x] = 1
           
#####################################################
def check_x():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    global board,game,go
    
    while y <= 2:
        if board[y][x] == 0:
            blank += 1

        if board[y][x] == 1:
            X += 1

        if board[y][x] == 2:
            O += 1


        if x == 2:
            x = -1
            y += 1
            if O == 3:
                print("\n")
                print("|Player2 wins!|")
                #print("X")
                game = False
            if X == 3:
                print("\n")
                print("|Player1 wins!|")
                game = False
                go = False
            X = 0
            O = 0
            
            
        x += 1
#####################################################       
def check_y():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    global board,game,go
    
    while x <= 2:
        if board[y][x] == 0:
            blank += 1

        if board[y][x] == 1:
            X += 1

        if board[y][x] == 2:
            O += 1


        if y == 2:
            y = -1
            x += 1
            
            if O == 3:
                print("\n")
                print("|Player2 wins!|")
                #print("Y")
                game = False
            if X == 3:
                print("\n")
                print("|Player1 wins!|")
                game = False
                go = False
            
            X = 0
            O = 0
            
            
        y += 1
    if blank == 0:
                print("\n")
                print("|Its a tie!|")
                game = False
#####################################################
def check_d():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    global board,game,go
    
    for g in range(3):
        if board[y][x] == 0:
            blank += 1

        if board[y][x] == 1:
            X += 1
            

        if board[y][x] == 2:
            O += 1
            


        if y == 2:
            y -= 1
            x += 1
            if O == 3:
                print("\n")
                #print("D")
                print("|Player2 wins!|")
                game = False
            if X == 3:
                print("\n")
                print("|Player1 wins!|")
                game = False
                go = False
            
            
            
        y += 1
        x += 1
        
#########################################################      
def check_d2():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    global board,game,go
   
    
    

    if board[0][2] == 1:
        X += 1
            

    if board[0][2] == 2:
        O += 1

        
    if board[1][1] == 1:
        X += 1
            

    if board[1][1] == 2:
        O += 1   

    if board[2][0] == 1:
        X += 1
            

    if board[2][0] == 2:
        O += 1      

    if O == 3:
        print("\n")
        #print("d2")
        print("|Player2 wins!|")
        game = False
    if X == 3:
        print("\n")
        print("|Player1 wins!|")
        game = False
        go = False
    if game == True:
        go = True
#####################################################################            
def check_x_c_2():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    blank_x = []
    blank_y = []
    global board,game,go
    
    while y <= 2:
        if board[y][x] == 0:
            blank += 1
            blank_x.append(x)
            blank_y.append(y)

        if board[y][x] == 1:
            X += 1

        if board[y][x] == 2:
            O += 1


        if x == 2:
            x = -1
            y += 1
            if O == 2 and go == True and blank == 1 :
                board[blank_y[0]][blank_x[0]] = 2
                print("\n")
                print_board()
                print("\n")
                #print("x2")
                print("|Player2 wins!|")
                game = False
                go = False
                
            X = 0
            O = 0
            blank = 0
            blank_x = []
            blank_y = []
            
        x += 1
def x_stopper():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    blank_x = []
    blank_y = []
    global board,game,go
    
    while y <= 2:
        if board[y][x] == 0:
            blank += 1
            blank_x.append(x)
            blank_y.append(y)

        if board[y][x] == 1:
            X += 1

        if board[y][x] == 2:
            O += 1
        if x == 2:
            x = -1
            y += 1    
            if X == 2 and go == True and blank == 1:
                    board[blank_y[0]][blank_x[0]] = 2
                    go = False
                    #print("x stoper")

            X = 0
            O = 0
            blank = 0
            blank = 0
            blank_x = []
            blank_y = []
            
            
        x += 1
######################################################################
def check_x_c_1():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    blank_x = []
    blank_y = []
    global board,game,go
    
    while y <= 2:
        if board[y][x] == 0:
            blank += 1
            blank_x.append(x)
            blank_y.append(y)

        if board[y][x] == 1:
            X += 1

        if board[y][x] == 2:
            O += 1


        if x == 2:
            x = -1
            y += 1
            if O == 1 and go == True and blank == 2:
                board[blank_y[0]][blank_x[random.randint(0,1)]] = 2
                go = False
                #print("x random")
            X = 0
            O = 0
            blank = 0
            blank_x = []
            blank_y = []
            
        x += 1
######################################################################
def check_r_c():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    blank_x = []
    blank_y = []
    global board,game,go
    
    while x <= 2:
        if board[y][x] == 0:
            blank += 1
            blank_x.append(x)
            blank_y.append(y)
            
        if y == 2:
            y = -1
            x += 1
            
        y += 1
    if go == True and blank >= 1 :
        num = random.randint(0,blank - 1)
        board[blank_y[num]][blank_x[num]] = 2
        go = False
            
        
######################################################################
def check_y_c_2():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    blank_x = []
    blank_y = []
    global board,game,go
    
    while x <= 2:
        if board[y][x] == 0:
            blank += 1
            blank_x.append(x)
            blank_y.append(y)

        if board[y][x] == 1:
            X += 1

        if board[y][x] == 2:
            O += 1


        if y == 2:
            y = -1
            x += 1
            
            if O == 2 and go == True and blank == 1 :
                board[blank_y[0]][blank_x[0]] = 2
                print("\n")
                print_board()
                print("\n")
                #print("y2")
                print("|Player2 wins!|")
                game = False
                go = False
            
            
            X = 0
            O = 0
            blank = 0
            blank_x = []
            blank_y = []
        y += 1
def y_stopper():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    blank_x = []
    blank_y = []
    global board,game,go
    while x <= 2:
        if board[y][x] == 0:
            blank += 1
            blank_x.append(x)
            blank_y.append(y)

        if board[y][x] == 1:
            X += 1

        if board[y][x] == 2:
            O += 1


        if y == 2:
            y = -1
            x += 1
            

            if X == 2 and go == True and blank == 1:
                board[blank_y[0]][blank_x[0]] = 2
                go = False
                #print("y stoper")
            X = 0
            O = 0
            blank = 0
            blank_x = []
            blank_y = []
            
        y += 1
        
##########################################################################
def check_y_c_1():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    blank_x = []
    blank_y = []
    global board,game,go
    
    while x <= 2:
        if board[y][x] == 0:
            blank += 1
            blank_x.append(x)
            blank_y.append(y)

        if board[y][x] == 1:
            X += 1

        if board[y][x] == 2:
            O += 1


        if y == 2:
            y = -1
            x += 1
            
            if O == 1 and go == True and blank == 2 :
                board[blank_y[random.randint(0,1)]][blank_x[0]] = 2
                go = False
                #print("y random")
            
            X = 0
            O = 0
            blank = 0
            blank_x = []
            blank_y = []
            
        y += 1                    
###############################
print_board()
while game == True:
    play()
    print_board()
    check_x()
    check_y()
    check_d()
    check_d2()
    check_x_c_2()
    check_y_c_2()
    y_stopper()
    x_stopper()
    if go == True:
        check_x_c_1()
        check_y_c_1()
        check_r_c()
    if game == True:
        print("\n")
        print_board()

        
