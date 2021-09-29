##GAME_OF_TicTacToe##
#board      #0/0      #2/2     #4/4
org_table=[['-',' | ','-',' | ','-'],
            #5/0     #7/2      #9/4
           ['-',' | ','-',' | ','-'],
            #10/0    #12/2     #14/4
           ['-',' | ','-',' | ','-']]
def table():
    global org_table
    for count in org_table:
        for i in count:
            print(i,end='')
        print()
def game():
    global org_table
    #userX
    try:
        user_input=int(input())
        if user_input>9 or user_input<=0:
            print('such place does not exist')
            raise ValueError
        else:
            if user_input==1 and org_table[0][0]!='O':
                org_table[0][0]='X'
            elif user_input==2 and org_table[0][2]!='O':
                org_table[0][2]='X'
            elif user_input==3 and org_table[0][4]!='O':
                org_table[0][4]='X'
            elif user_input==4 and org_table[1][0]!='O':
                org_table[1][0]='X'
            elif user_input==5 and org_table[1][2]!='O':
                org_table[1][2]='X'
            elif user_input==6 and org_table[1][4]!='O':
                org_table[1][4]='X'
            elif user_input==7 and org_table[2][0]!='O':
                org_table[2][0]='X'
            elif user_input==8 and org_table[2][2]!='O':
                org_table[2][2]='X'
            elif user_input==9 and org_table[2][4]!='O':
                org_table[2][4]='X'
            winner()
            table()
            # winner()
            # if winner() == 3:
            #     print('Game Over')
            #     return print('X Wins')
    except ValueError:
        print('''Try Again, this time try in the Range 1-9''')
        user_input=int(input())
        if user_input == 1 and org_table[0][0] != 'O':
            org_table[0][0] = 'X'
        elif user_input == 2 and org_table[0][2] != 'O':
            org_table[0][2] = 'X'
        elif user_input == 3 and org_table[0][4] != 'O':
            org_table[0][4] = 'X'
        elif user_input == 4 and org_table[1][0] != 'O':
            org_table[1][0] = 'X'
        elif user_input == 5 and org_table[1][2] != 'O':
            org_table[1][2] = 'X'
        elif user_input == 6 and org_table[1][4] != 'O':
            org_table[1][4] = 'X'
        elif user_input == 7 and org_table[2][0] != 'O':
            org_table[2][0] = 'X'
        elif user_input == 8 and org_table[2][2] != 'O':
            org_table[2][2] = 'X'
        elif user_input == 9 and org_table[2][4] != 'O':
            org_table[2][4] = 'X'
        winner()
        table()
    #userY
    try:
        user_input=int(input())
        if user_input>9 or user_input<=0:
            print('such place does not exist')
            raise ValueError
        else:
            if user_input==1 and org_table[0][0]!='X':
                org_table[0][0]='O'
            elif user_input==2 and org_table[0][2]!='X':
                org_table[0][2]='O'
            elif user_input==3 and org_table[0][4]!='X':
                org_table[0][4]='O'
            elif user_input==4 and org_table[1][0]!='X':
                org_table[1][0]='O'
            elif user_input==5 and org_table[1][2]!='X':
                org_table[1][2]='O'
            elif user_input==6 and org_table[1][4]!='X':
                org_table[1][4]='O'
            elif user_input==7 and org_table[2][0]!='X':
                org_table[2][0]='O'
            elif user_input==8 and org_table[2][2]!='X':
                org_table[2][2]='O'
            elif user_input==9 and org_table[2][4]!='X':
                org_table[2][4]='O'
            winner()
            table()
            # winner()
            # if winner() == 3:
            #     print('Game Over')
            #     return print('O Wins')
    except ValueError:
        print('''Try Again, this time try in the Range 1-9''')
        user_input=int(input())
        if user_input == 1 and org_table[0][0] != 'X':
            org_table[0][0] = 'O'
        elif user_input == 2 and org_table[0][2] != 'X':
            org_table[0][2] = 'O'
        elif user_input == 3 and org_table[0][4] != 'X':
            org_table[0][4] = 'O'
        elif user_input == 4 and org_table[1][0] != 'X':
            org_table[1][0] = 'O'
        elif user_input == 5 and org_table[1][2] != 'X':
            org_table[1][2] = 'O'
        elif user_input == 6 and org_table[2][4] != 'X':
            org_table[2][4] = 'O'
        elif user_input == 7 and org_table[2][0] != 'X':
            org_table[2][0] = 'O'
        elif user_input == 8 and org_table[2][2] != 'X':
            org_table[2][2] = 'O'
        elif user_input == 9 and org_table[2][4] != 'X':
            org_table[2][4] = 'O'
        winner()
        table()
def winner():
    #coloumn_checker
    for count in org_table:
        X=0
        O=0
        for i in count:
            if i=='X':
                X+=1
            elif i=='O':
                O+=1
        if X==3 and O==3:
            print('''It is a draw.Game Over''')
            break
        elif X==3:
            print('''X wins.Game Over''')
            break
        elif O==3:
            print('''O wins.Game Over''')
            break
        X=0
        O=0
    #Row_Checker
    # for count in org_table:
    #     if count[]
