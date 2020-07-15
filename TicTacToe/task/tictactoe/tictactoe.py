user = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
coord = [[], [0, user[6], user[3], user[0]], [0, user[7], user[4], user[1]], [0, user[8], user[5], user[2]]]


def status():
    print(f"---------\n"
          f"| {coord[1][3]} {coord[2][3]} {coord[3][3]} |\n"
          f"| {coord[1][2]} {coord[2][2]} {coord[3][2]} |\n"
          f"| {coord[1][1]} {coord[2][1]} {coord[3][1]} |\n"
          f"---------")


def check_win(grid, player):
    if grid[1][1] == player and grid[1][2] == player and grid[1][3] == player:
        print(f"{player} wins")
        exit()
    elif grid[2][1] == player and grid[2][2] == player and grid[2][3] == player:
        print(f"{player} wins")
        exit()
    elif grid[3][1] == player and grid[3][2] == player and grid[3][3] == player:
        print(f"{player} wins")
        exit()
    elif grid[1][1] == player and grid[2][1] == player and grid[3][1] == player:
        print(f"{player} wins")
        exit()
    elif grid[1][2] == player and grid[2][2] == player and grid[3][2] == player:
        print(f"{player} wins")
        exit()
    elif grid[1][3] == player and grid[2][3] == player and grid[3][3] == player:
        print(f"{player} wins")
        exit()
    elif grid[1][1] == player and grid[2][2] == player and grid[3][3] == player:
        print(f"{player} wins")
        exit()
    elif grid[1][3] == player and grid[2][2] == player and grid[3][1] == player:
        print(f"{player} wins")
        exit()
    return False


def free_space(grid):
    for x in range(1, 4):
        for y in range(1, 4):
            if ' ' in grid[x][y]:
                return True


def move(player):
    move_x, move_y = map(int, input("Enter the coordinates:").split(' '))
    occupied(move_x, move_y, player)


def occupied(x, y, player):
    if type(x) and type(y) is int:
        if x <= 3 and y <= 3:
            if coord[x][y] in [' ', '_']:
                coord[x][y] = player
                status()
                check_win(coord, player)
                if not check_win(coord, 'X') and not free_space(coord):
                    print("Draw")
                    exit()
                if not check_win(coord, 'O') and not free_space(coord):
                    print("Draw")
                    exit()
            else:
                print("This cell is occupied! Choose another one!")
                move(player)
        else:
            print("Coordinates should be from 1 to 3!")
            move(player)
    else:
        print("You should enter numbers!")
        move(player)


status()
while True:
    move('X')
    move('O')
