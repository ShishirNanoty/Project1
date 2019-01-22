"""
0 | | | | |
1 ---------
2 | | | | |
3 ---------
4 | | | | |
5 ---------
6 | | | | |
  012345678
"""
def cnkt4(track):
    for row in range(7):
        if row%2 == 0:
            actualrow = int(row/2)
            for col in range(9):
                if col%2 != 0:
                    actualcol = int(col/2)
                    print(track[actualcol][actualrow], end='')
                else:
                    if col != 8:
                        print('|', end='')
                    else: print('|')
        else:
            print('---------')
player = 1
track = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
def chkrow(col):
    try:
        for row in range(3, -1 , -1):
            if track[col][row] == " ":
                actrow = row
                break
        return actrow
    except:
        print('Invalid move')

def chkwin(track,win1_cnt,win2_cnt,act_player):
    win1 = False
    win2 = False
    win3 = False
    for col in range(4):
        for row in range(3,0,-1):
            if track[col][row] != track[col][row-1] or track[col][row] == " ":
                win1 = False
                win1_cnt = 0
                # print(col,row,'Here win1 is false')
                break
            else:
                win1 = True
                win1_cnt = win1_cnt + 1
                # print(col,row,'Here win1 is true &', win1_cnt)
                if win1_cnt == 3 or win2_cnt == 3:
                    print('Player', act_player, 'Wins')
                continue
            break
        # break
    for row in range(3,0,-1):
        for col in range(3):
            if track[col][row] != track[col+1][row] or track[col][row] == " ":
                win2 = False
                win2_cnt = 0
                # print(col,row,'here win2 is false')
                break
            else:
                win2 = True
                win2_cnt = win2_cnt + 1
                # print(col,row,'here win2 is true &',win2_cnt)
                if win1_cnt == 3 or win2_cnt == 3:
                    print('Player', act_player, 'Wins')
                continue
            break
        # break
    if win1 == True or win2 == True:
        win = True
    else: win = False
    return win, win1_cnt,win2_cnt

win = False
win1_cnt = 0
win2_cnt = 0
while True:
    play = input('Enter C to continue\n')
    if play == 'C' or play == 'c':
        try:
            print('Player', player,'turn')
            col = int(input('Enter col>>'))
            row = chkrow(col)
            if player == 1:
                track[col][row] = 'X'
                player = 2
                act_player = 1
            else:
                track[col][row] = 'O'
                player = 1
                act_player = 2
            print(track)
            win = chkwin(track,win1_cnt,win2_cnt,act_player)
            # print(win)
            cnkt4(track)

        except:
            print('pls try again')
    else:
        print('Done!')
