import re

with open('Day22/input.txt') as file:
    lines = [line for line in file]

W=set()
F=set()
# I=[]
start=None
for row,line in enumerate(lines):
    for column,item in enumerate(line):
        if line[0] not in [' ','.','#']:
            instructions=re.split('([R,L])',line)
        else:
            if item=='.':
                if start is None:
                    start=(row,column)
                F.add((row,column))
            elif item=='#':
                W.add((row,column))

ALL=W|F
maxrow = max([row for row,column in ALL])
maxcolumn = max([column for row,column in ALL])
minrow = min([row for row,column in ALL])
mincolumn = min([column for row,column in ALL])

EDGE = {}
for i in range(0,50):
    EDGE[(-1,50+i)]=(150+i,0),(0,1)
    EDGE[(150+i,-1)]=(0,50+i),(1,0)

    EDGE[(50+i,50-1)]=(100,0+i),(1,0)
    EDGE[(100-1,0+i)]=(50+i,50),(0,1)

    EDGE[(0+i,50-1)]=(149-i,0),(0,1)
    EDGE[(149-i,-1)]=(0+i,50),(0,1)
    
    EDGE[(-1,100+i)]=(199,0+i),(-1,0)
    EDGE[(199+1,0+i)]=(0,100+i),(1,0)

    EDGE[(49+1,100+i)]=(50+i,99),(0,-1)
    EDGE[(50+i,99+1)]=(49,100+i),(-1,0)

    EDGE[(0+i,149+1)]=(149-i,99),(0,-1)
    EDGE[(149-i,99+1)]=(0+i,149),(0,-1)
    
    EDGE[(149+1,50+i)]=(150+i,49),(0,-1)
    EDGE[(150+i,49+1)]=(149,50+i),(-1,0)

def rotate(d,n):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    return directions[(directions.index(d)+n)%len(directions)]

def step(start,d,part=1):
    tentative = (start[0]+d[0],start[1]+d[1])
    dt = d
    if tentative in EDGE.keys() and part==2:
        tentative,dt = EDGE[tentative]
    if tentative in W:
        return start,d
    elif tentative in F:
        return tentative,dt
    elif part==1:
        if d==(0,1):
            search = (start[0],mincolumn)
        elif d==(1,0):
            search = (minrow,start[1])
        elif d==(0,-1):
            search = (start[0],maxcolumn)
        elif d==(-1,0):
            search = (maxrow,start[1])
        else:
            assert False, d
        while search not in ALL:
            search = (search[0]+d[0],search[1]+d[1])
        if search in W:
            return start,d
        elif search in F:
            return search,d
        else:
            assert False,search
    else:
        assert False, (start,tentative,d,dt)

d = (0,1)
pos = start

for item in instructions:
    if item=='R':
        d = rotate(d,1)  
    elif item=='L':
        d = rotate(d,-1)
    else:
        for _ in range(int(item)):
            pos,d = step(pos,d,part=1)

directions = [(0,1),(1,0),(0,-1),(-1,0)]

print('------------------------')
print('Part1:',1000*(pos[0]+1)+4*(pos[1]+1)+directions.index(d))
print('------------------------')

d = (0,1)
pos = start

for item in instructions:
    if item=='R':
        d = rotate(d,1)  
    elif item=='L':
        d = rotate(d,-1)
    else:
        for _ in range(int(item)):
            pos,d = step(pos,d,part=2)

print('Part 2:',1000*(pos[0]+1)+4*(pos[1]+1)+directions.index(d))
print('------------------------')