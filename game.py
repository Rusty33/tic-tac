board = [[0,0,0],[0,0,0],[0,0,0]]
turn = 1
game = True
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
            board[y][x] = turn
            if turn == 1:
                turn = 2
            else:
                turn = 1
#####################################################
def check_x():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    global board,game
    
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
                game = False
            if X == 3:
                print("\n")
                print("|Player1 wins!|")
                game = False
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
    global board,game
    
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
                game = False
            if X == 3:
                print("\n")
                print("|Player1 wins!|")
                game = False
            
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
    global board,game
    
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
                print("|Player2 wins!|")
                game = False
            if X == 3:
                print("\n")
                print("|Player1 wins!|")
                game = False
            
            
            
        y += 1
        x += 1
        
#########################################################      
def check_d2():
    x = 0
    y = 0
    O = 0
    X = 0
    blank = 0
    global board,game
   
    
    

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
        print("|Player2 wins!|")
        game = False
    if X == 3:
        print("\n")
        print("|Player1 wins!|")
        game = False
            
            
            
        
###############################
print_board()
while game == True:
    
    play()
    print_board()
    check_x()
    check_y()
    check_d()
    check_d2()

        
