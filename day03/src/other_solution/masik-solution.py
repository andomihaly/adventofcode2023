import math as m, re

board = list(open('advent_day3_e1.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
         if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

file1 = open("other-solution.txt", "a")
for p in chars.values():
    for n in p:
        file1.write(str(n)+"\n")
file1.close()
print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))