

p1_win = {1: 'x|x|x', 2: ('x', 'x', 'x')}
p2_win = {1: 'o|o|o', 2: ('o', 'o', 'o')}

Player = 0

rows = {1: 'x|#|#', 2: 'x|x|#', 3: 'x|#|x'}
rows_list = list(rows.values())
p1win_list = list(p1_win.values())
p2win_list = list(p2_win.values())

line1 = rows_list[0][0], rows_list[1][0], rows_list[2][0]
line2 = rows_list[0][2], rows_list[1][2], rows_list[2][2]
line3 = rows_list[0][4], rows_list[1][4], rows_list[2][4]

angle1 = rows_list[0][0], rows_list[1][2], rows_list[2][4]
angle2 = rows_list[0][4], rows_list[1][2], rows_list[2][0]

if angle1 in p1win_list or angle2 in p1win_list:
    print('Player 1 win')
if line1 in p1win_list or line2 in p1win_list or line3 in p1win_list:
    print('Player 1 win')





print(f'{rows_list[0]}\n{rows_list[1]}\n{rows_list[2]} ')

