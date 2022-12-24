import sys

filename = sys.argv[1] if len(sys.argv)>1 else 'input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

E=set()
for x,line in enumerate(lines):
    for y,item in enumerate(line):
        if item=='#':
            E.add((x,y))

NORTH=[(-1,0),(-1,1),(-1,-1)]
SOUTH=[(1,0),(1,-1),(1,1)]
WEST=[(0,-1),(-1,-1),(1,-1)]
EAST=[(0,1),(1,1),(-1,1)]
D = [NORTH,SOUTH,WEST,EAST]

MOVES={}

def print_elves(E,MOVES):
    xmin=1000
    xmax=-1000
    ymin=1000
    ymax=-1000
    for x,y in E:
        if x<xmin:
            xmin=x
        if y<ymin:
            ymin=y
        if x>xmax:
            xmax=x
        if y>ymax:
            ymax=y
    moves = [MOVES[key] for key in MOVES.keys()]
    for row in range(xmin-10,xmax+10):
        toprint=''
        for column in range(ymin-10,ymax+10):
            if (row,column) in E:
                toprint+='#'
            elif (row,column) in moves:
                toprint+='o'
            else:
                toprint+='.'
        print(toprint)

def count_empty(E):
    xmin=1000
    xmax=-1000
    ymin=1000
    ymax=-1000
    for x,y in E:
        if x<xmin:
            xmin=x
        if y<ymin:
            ymin=y
        if x>xmax:
            xmax=x
        if y>ymax:
            ymax=y
    count=0
    for x in range(xmin,xmax+1):
        for y in range(ymin,ymax+1):
            if (x,y) not in E:
                count+=1
    return count

for i in range(1000):
    for elf in E:
        stay=True
        for d in D:
            op = True
            for k in d:
                x,y = elf
                dx,dy = k
                xx = x+dx
                yy = y+dy
                if (xx,yy) in E:
                    op = False
                    stay = False
            if op:
                if elf not in MOVES.keys():
                    MOVES[elf]=(elf[0]+d[0][0],elf[1]+d[0][1])
        if stay:
            del MOVES[elf]

    if len(MOVES.keys())==0:
        print('Part 2:',i+1)
        print('------------------------')
        break

    for key in MOVES.keys():
        mymove = MOVES[key]
        othermoves = [MOVES[v] for v in MOVES.keys() if v!=key]
        if mymove not in othermoves:
            E.remove(key)
            E.add(mymove)

    m = D.pop(0)
    D.append(m)
    MOVES={}
    if i==9:
        print('------------------------')
        print('Part 1:',count_empty(E))
        print('------------------------')
