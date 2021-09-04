# noughts and crosses by Evlakhov FPW37
my_field = []

# making restart of the game function
def re_start():
    my_field = [[' ', '0', '1', '2'], ['0', '-', '-', '-'], ['1', '-', '-', '-'], ['2', '-', '-', '-']]
    # create picture of start game field
    print()
    for i in range(len(my_field)):
        for j in range(len(my_field[i])):
            print(my_field[i][j], end=" ")
        print()

    print()
    print("""New game! Type "s" for stop, "n" for restart game""")
    print("Make a move typing number of the field. First vertical, then horizontal line.")
    print()
    return my_field

# create picture of start game field
def making_picture(vertical, horizontal, num, figure, my_field):

    if my_field[vertical+1][horizontal+1] == "-":
        my_field[vertical+1][horizontal+1] = figure 
    else:
        print('this field is taken, try another:')
        print(my_field)
        return making_picture(player_input(num, "vertical", figure), player_input(num, "horizontal", figure), num, figure, my_field)

    for i in range(len(my_field)):
        for j in range(len(my_field[i])):
            print(my_field[i][j], end=" ")
        print()
    print()

my_non_stop = True

# start game
def game_loop(my_field):

    while(my_non_stop):
        p_1_vertic = player_input(1, "vertical", "x")
        p_1_horizont = player_input(1, "horizontal", "x")
        making_picture(p_1_vertic, p_1_horizont, 1, "x", my_field)
        check_field(1, "x", my_field)

        p_2_vertic = player_input(2, "vertical", "0")
        p_2_horizont = player_input(2, "horizontal", "0")
        making_picture(p_2_vertic, p_2_horizont, 2, "0", my_field)
        check_field(2, "0", my_field)

       # my_non_stop = False

#making_input with check
def player_input(num, direction, figure):
    some_player_input = input(f"player {num} input a move by {figure}, {direction} line: ")
    if(some_player_input == "s"): 
        print("game stopped!")
        exit()
    elif(some_player_input == "n"):
        print("New game!")
        my_non_stop = False
        game_loop(re_start())
    else:
        try:
            some_player_input = int(some_player_input)
        except ValueError:
            print("Wrong input, try one more")
            print()
            some_player_input = player_input(num, direction, figure)
        #check if we in range of game field
        if(int(some_player_input) > len(my_field)-2):
            print(f"Just numbers from 0 to {len(my_field)-2}, try one more")
            print()
            some_player_input = player_input(num, direction, figure)
    
    return some_player_input

#restart_check():
#    my_choose = input("restart game or stop? (r/s): ")
#    if(some_player_input == "s"): 
#        print("game stopped!")
#        exit()
#    elif(some_player_input == "n"):
#        print("New game!")
#        my_non_stop = False
#        my_field = re_start()
#    else:


#winner picture
def win_pict(num):
    print("*" * 30)
    print(f"*        PLAYER {num} WIN!       *")
    print("*" * 30)
    my_field = re_start()
    game_loop(my_field)

#nobody win picture
def nobody_win_pict():
    print("*" * 30)
    print(f"*        NOBODY WIN!       *")
    print("*" * 30)
    my_field = re_start()
    game_loop(my_field)


#check the game state
def check_field(num, figure, my_field):
    match_list = [36, 63, 66, 69, 96] #if sum of count_ver and count_hor match with the list element = win
    match_flag = 0
    empty_field_flag = 0
    index_counter = 0
    count_ver = 0
    count_hor = 0
    empty_field = '-'

    #nobody win check
    for t in range(len(my_field)):
        empty_field_flag += 1 if empty_field in my_field[t] else 0
    if empty_field_flag == 0:
        my_non_stop = False
        nobody_win_pict()
        return my_non_stop

    for i in range(1, len(my_field)):
        count_ver += 1
        count_hor = 0
        #print("count_ver - ", count_ver)
        for j in range(1, len(my_field)):
            count_hor += 1
           # print("count_hor - ", count_hor)
            if my_field[i][j] == figure:
                match_flag += 1
                index_counter += int(str(count_ver) + str(count_hor))
               # print("count_ver - ", count_ver, "; count_hor - ", count_hor, "; fig - ",  figure)
                #print("index_counter", index_counter)

    if(index_counter in match_list and match_flag > 1):
        #print(f"Player {num} with {figure} win!")
        my_non_stop = False
        win_pict(num)
            #restart_check() 
        return my_non_stop
                
#        for j in range(len(my_field)):
 #           if my_field[i][j] 

# make game filed matrix
my_field = re_start()
game_loop(my_field)
