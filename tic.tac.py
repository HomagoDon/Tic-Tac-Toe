game_win = {1: 'x|x|x', 2: ('x', 'x', 'x')}


Player = 0
rows = {1: 'x|#|#', 2: 'x|#|#', 3: 'x|#|#'}
rows_list = list(rows.values())
win_list = list(game_win.values())

line1 = rows_list[0][0], rows_list[1][0], rows_list[2][0]
line2 = rows_list[0][2], rows_list[1][2], rows_list[2][2]
line3 = rows_list[0][4], rows_list[1][4], rows_list[2][4]

angle1 = rows_list[0][0], rows_list[1][2], rows_list[2][4]
angle2 = rows_list[0][4], rows_list[1][2], rows_list[2][0]


print(line1, line2, line3)
print(angle1, angle2)




print(f'{rows_list[0]}\n{rows_list[1]}\n{rows_list[2]} ')

