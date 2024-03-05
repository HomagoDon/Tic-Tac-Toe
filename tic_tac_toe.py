Player1 = 0

# Win Conditions 
PlayerX_Win = ['x|x|x', ('x', 'x', 'x')]
PlayerO_Win = ['o|o|o', ('o', 'o', 'o')]

# Game board
rows = {1: '#|#|#', 2: '#|#|#', 3: '#|#|#'}
rows_list = list(rows.values())
Board = rows_list[0] + '\n' + rows_list[1] + '\n' + rows_list[2]

# All the three columns
column1 = rows_list[0][0], rows_list[1][0], rows_list[2][0]
column2 = rows_list[0][2], rows_list[1][2], rows_list[2][2]
column3 = rows_list[0][4], rows_list[1][4], rows_list[2][4]
columns = column1, column2, column3

#First and second board angles
angle1 = rows_list[0][0], rows_list[1][2], rows_list[2][4]
angle2 = rows_list[0][4], rows_list[1][2], rows_list[2][0]
angles = angle1, angle2

#Game Start
Player1 = input("X or O? ").lower()
while Player1 != 'x' and Player1 != 'o':
    Player1 = input("Wrong input! Choose X or O: ").lower()

if Player1 == 'x':
    print('Player 1 is X \nPlayer 2 is O')
elif Player1 == 'o':
    print('Player 1 is O \nPlayer 2 is X')

#Check for Player win
if PlayerX_Win[1] in columns or PlayerX_Win[1] in angles or PlayerX_Win[0] in rows_list:
    print('Player X won!')
if PlayerO_Win[1] in columns or PlayerO_Win[1] in angles or PlayerO_Win[0] in rows_list:
    print('Player O won!')
