from globals import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWw',
    'W...w.......w..W...........w',
    'W.....wwww..w..W...w.w.w.w.w',
    'W.......w...w..W.w..w.w.w..w',
    'Wwwwwww........W.www.......w',
    'W...........wwwW...W.......w',
    'W...w..........W...Wwww.wwww',
    'W...w.......w..W...W',
    'W...w.......w..W...W',
    'W...w.......w......W',
    'W...w.......w..Wwwww...',
    'Ww.wWWWWWWWWWWWWwwwwwwwwwww.www',
    'w.............................w',
    'w....w.w.w.w.w.w.w.w.w.w..ww..w',
    'w.........................ww..w',
    'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
]

world_map =set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W' or char == 'w':
            world_map.add((i * TILE, j * TILE))