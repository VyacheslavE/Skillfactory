# ______________ sea_battle. Evlakhov FPW-37

from random import randrange


class Battle_board:
    def create_field(self):
        return [["   ", "| 1 |", "| 2 |", "| 3 |", "| 4 |", "| 5 |", "| 6 |"],
                [" 1 ", "| O |", "| O |", "| O |", "| O |", "| O |", "| O |"],
                [" 2 ", "| O |", "| O |", "| O |", "| O |", "| O |", "| O |"],
                [" 3 ", "| O |", "| O |", "| O |", "| O |", "| O |", "| O |"],
                [" 4 ", "| O |", "| O |", "| O |", "| O |", "| O |", "| O |"],
                [" 5 ", "| O |", "| O |", "| O |", "| O |", "| O |", "| O |"],
                [" 6 ", "| O |", "| O |", "| O |", "| O |", "| O |", "| O |"]]


# -- show battle field for the player
def show_the_field(player1, player2):
    print("                   Player 1                                  Player 2(computer)")
    for i in range(len(player1)):
        print(*player1[i], "   |||  ", *player2[i])


# arranging ships by user
def aks_coord(counter, param_2, j):
    while True:
        print()
        coord = input(f"""Input "{counter}" X Y positions of the {param_2}: """).split()
        print()

        if len(coord) < 2:
            print("Should be two coordinates!")
            continue
        x, y = coord

        if not (x.isdigit() and y.isdigit()):
            print("Should be numbers only!")
            continue
        x, y = int(x), int(y)

        if 1 > x or x > 6 or 1 > y or y > 6:
            print("Coordinates out of field!")
            continue

        if player_1_marked[x][y] != "| O |":
            print("Field has taken!")
            continue

        # check if around empty fields
        matches_flag = 0

        for h in [-1, 0, 1]:
            if not ((h + x == 0) or (h + x == 7)):
                for s in [-1, 0, 1]:
                    if not ((s + y == 0) or (s + y == 7)):
                        try:
                            if player_1_marked[x + h][y + s] != "| O |":
                                temp_list = [x + h, y + s]
                                if temp_list not in j:
                                    matches_flag += 1
                        except IndexError as e:
                            continue

        # check flag if around empty fields
        if matches_flag > 0:
            print("Around must be empty fields!")
            continue

        if counter == 2 and (j[0][0] - x) > 1:
            print("Coordinates of one ship must be nearby!")
            continue

        if counter == 2 and (j[0][1] - y) > 1:
            print("Coordinates of one ship must be nearby!")
            continue

        if counter == 3 and (j[1][0] - x) > 1:
            print("Coordinates of one ship must be nearby!")
            continue

        if counter == 3 and (j[1][1] - y) > 1:
            print("Coordinates of one ship must be nearby!")
            continue

        if counter == 3:
            print(counter == 3 and ((j[0][0] == j[1][0] and j[0][0] == x) or (j[0][1] == j[1][1] and j[0][1] == y)))

        if counter == 3 and not ((j[0][0] == j[1][0] and j[0][0] == x) or (j[0][1] == j[1][1] and j[0][1] == y)):
            print("Coordinates of one ship must be in one line!")
            continue

        return x, y


# additional try to find empty fields in automatic way
def coordinates_helper(player):
    for x_coord in range(1, 7):
        for y_coord in range(1, 7):
            match_flag = 0
            if player[x_coord][y_coord] == "| O |":
                for h in [-1, 0, 1]:
                    if not ((h + x_coord == 0) or (h + x_coord == 7)):
                        for s in [-1, 0, 1]:
                            if not ((s + y_coord == 0) or (s + y_coord == 7)):
                                try:
                                    if player[x_coord + h][y_coord + s] != "| O |":
                                        match_flag += 1
                                except IndexError as e:
                                    continue
            if match_flag == 0:
                yield x_coord, y_coord


# violation of rules try to arrange if there is no enough empty space on field
# there's ignored ships nearby in diagonal line
def coordinates_helper_violations(player):
    for x_coord in range(1, 7):
        for y_coord in range(1, 7):
            match_flag = 0
            if player[x_coord][y_coord] == "| O |":
                for h in [-1, 0, 1]:

                    if not ((h + x_coord == 0) or (h + x_coord == 7)):
                        try:
                            if player[x_coord + h][y_coord] != "| O |":
                                match_flag += 1
                        except IndexError as e:
                            continue

                    if not ((h + y_coord == 0) or (h + y_coord == 7)):
                        try:
                            if player[x_coord][y_coord + h] != "| O |":
                                match_flag += 1
                        except IndexError as e:
                            continue

                if match_flag == 0:
                    return x_coord, y_coord


# arranging ships by computer
def aks_coord_computer(player2, j):
    loop_counter = 0
    while True:
        loop_counter += 1
        if loop_counter < 1000:
            # make random coordinates and direction
            x_coord = randrange(1, 7)
            y_coord = randrange(1, 7)
            direction = randrange(0, 2)

        # if loop works too long try first try to arrange:
        elif 1000 <= loop_counter <= 1035:
            for x1, y1 in coordinates_helper(player2):
                x_coord, y_coord = x1, y1
        elif loop_counter > 1010:
            x_coord, y_coord = coordinates_helper_violations(player2)

            return x_coord, y_coord

        # make tree deck ship coordinates
        if direction and len(j) == 3:
            # shift the ship by vertical line if we're rich edge of the field
            y_coord = y_coord - 1 if y_coord == 5 else y_coord - 2 if y_coord == 6 else y_coord
            x2_coord, x3_coord = x_coord, x_coord
            y2_coord, y3_coord = y_coord + 1, y_coord + 2

            return x_coord, y_coord, x2_coord, y2_coord, x3_coord, y3_coord

        elif len(j) == 3:
            # shift the ship by horizontal line if we're rich edge of the field
            x_coord = x_coord - 1 if x_coord == 5 else x_coord - 2 if x_coord == 6 else x_coord
            y2_coord, y3_coord = y_coord, y_coord
            x2_coord, x3_coord = x_coord + 1, x_coord + 2

            return x_coord, y_coord, x2_coord, y2_coord, x3_coord, y3_coord

        # make two deck ships coordinates
        if direction and len(j) == 2:
            # shift if we're rich edge of field
            y_coord = y_coord - 1 if y_coord == 6 else y_coord
            x2_coord = x_coord
            y2_coord = y_coord + 1
        elif len(j) == 2:
            # shift if we're rich edge of field
            x_coord = x_coord - 1 if x_coord == 6 else x_coord
            y2_coord = y_coord
            x2_coord = x_coord + 1

        # check if field were taken before
        if len(j) == 2 and (player2[x_coord][y_coord] != "| O |" or player2[x2_coord][y2_coord] != "| O |"):
            continue

        match_flag = 0
        if len(j) == 2:
            # check if around empty fields
            for h in [-1, 0, 1]:
                for s in [-1, 0, 1]:
                    try:
                        if player2[x_coord + h][y_coord + s] != "| O |":
                            if [x_coord + h] != x2_coord and [y_coord + s] != y2_coord:
                                match_flag += 1

                        if player2[x2_coord + h][y2_coord + s] != "| O |":
                            match_flag += 1

                    except IndexError as e:
                        continue

        if len(j) == 2 and match_flag == 0:
            return x_coord, y_coord, x2_coord, y2_coord
        elif len(j) == 2 and match_flag != 0:
            continue

        # check if field were taken before
        if player2[x_coord][y_coord] != "| O |":
            continue

        match_flag_single = 0
        for h in [-1, 0, 1]:
            if not ((h + x_coord == 0) or (h + x_coord == 7)):
                for s in [-1, 0, 1]:
                    if not ((s + y_coord == 0) or (s + y_coord == 7)):
                        try:
                            if player2[x_coord + h][y_coord + s] != "| O |":
                                match_flag_single += 1
                        except IndexError as e:
                            continue

        if match_flag_single == 0:
            return x_coord, y_coord


# choose ships start positions:
def choose_positions(player, player2):
    ship_set = {"Thee deck ship": [[], [], []],
                "Two deck ship 1": [[], []],
                "Two deck ship 2": [[], []],
                "One deck ship 1": [[]],
                "One deck ship 2": [[]],
                "One deck ship 3": [[]],
                "One deck ship 4": [[]]}
    for i, j in ship_set.items():
        counter = 0
        counter_in_ship_set = 0
        for k in j:
            counter += 1
            k = list(aks_coord(counter, i, ship_set[i]))
            player[k[0]][k[1]] = "| ■ |"
            ship_set[i][counter_in_ship_set] = k
            # clearConsole()
            show_the_field(player, player2)
            counter_in_ship_set += 1
    print("ships are ready for battle!")
    return ship_set


# computer chose the positions
def choose_positions_computer(player2):
    ship_set = {"Thee deck ship": [[], [], []],
                "Two deck ship 1": [[], []],
                "Two deck ship 2": [[], []],
                "One deck ship 1": [[]],
                "One deck ship 2": [[]],
                "One deck ship 3": [[]],
                "One deck ship 4": [[]]}

    for i, j in ship_set.items():
        v = list(aks_coord_computer(player2, ship_set[i]))
        counter = 0
        for r in range(0, len(v) - 1, 2):
            player2[v[r]][v[r + 1]] = "| ■ |"
            ship_set[i][counter] = v[r], v[r + 1]
            counter += 1

    return ship_set


def check_if_not_dead(plr):
    my_counter = 0
    for a in plr:
        for b in a:
            if b == "| X |":
                my_counter += 1
    if my_counter == 11:
        return True

    return False


# making shots
def player_shot(player2_m, player1, player2):
    while True:
        print()
        coord = input(f"""Make a shot X Y positions: """).split()
        print()

        if len(coord) < 2:
            print("Should be two coordinates!")
            continue
        x, y = coord

        if not (x.isdigit() and y.isdigit()):
            print("Should be numbers only!")
            continue
        x, y = int(x), int(y)

        if 1 > x or x > 6 or 1 > y or y > 6:
            print("Coordinates out of field!")
            continue

        if player2[x][y] == "| T |" or player2[x][y] == "| X |":
            print("""You've already shot here!""")
            continue

        if player2_m[x][y] != "| O |":
            player2[x][y] = "| X |"
            show_the_field(player1, player2)
            if check_if_not_dead(player2):
                print("All ships hit! YOU WIN!")
                exit()
            print("** Hit! **")
            print("Shot one more!")
            continue
        else:
            player2[x][y] = "| T |"
            show_the_field(player1, player2)
            print("you miss :(")
            return


def computer_shot(player1_m, player1, player2):
    while True:
        # make random coordinates
        x = randrange(1, 7)
        y = randrange(1, 7)
        if player1[x][y] == "| T |" or player1[x][y] == "| X |":
            continue
        if player1_m[x][y] != "| O |":
            player1[x][y] = "| X |"
            show_the_field(player1, player2)
            if check_if_not_dead(player1):
                print("All ships hit! COMPUTER WIN!")
                exit()
            print("(((  Hit! )))")
            print("Computer shoots one more!")
            continue
        else:
            player1[x][y] = "| T |"
            show_the_field(player1, player2)
            print("computer miss!")
            return


# --create players
player_1 = Battle_board().create_field()
player_2 = Battle_board().create_field()
player_1_marked = Battle_board().create_field()
player_2_marked = Battle_board().create_field()

# --show player 1 battle field to arrange ships
show_the_field(player_1, player_2)

player2_positions = choose_positions_computer(player_2_marked)
print("Computers ships are ready for battle!")

choose_who_arrange = input("Automatic arrange or manual? Press 'm' for manual or any letter for auto arrange:")

# chose who mill arrange ships user or computer
if choose_who_arrange.lower() == 'm':
    player1_positions = choose_positions(player_1_marked, player_2) #put player_2_marked insdead player_2 to see
else:
    player1_positions = choose_positions_computer(player_1_marked)  # change after to player_2, player_2

show_the_field(player_1_marked, player_2) #put player_2_marked insdead player_2 to see
print("All the ships are ready for battle!")

print()
print("""************** START BATTLE! **************""")

move_counter = 0
while True:
    if move_counter % 2 == 0:
        player_shot(player_2_marked, player_1, player_2)
    else:
        print("Computer's move: ")
        computer_shot(player_1_marked, player_1, player_2)

    move_counter += 1

