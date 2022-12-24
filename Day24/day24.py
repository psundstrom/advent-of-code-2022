from collections import deque

import sys

filename = sys.argv[1] if len(sys.argv)>1 else 'input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

S = (0,1)
W = set()
B = []
DB = []
for r,line in enumerate(lines):
    for c,item in enumerate(line):
        if item == '#':
            W.add((r,c))
        elif item == '<':
            B.append((r,c))
            DB.append((0,-1))
        elif item == '>':
            B.append((r,c))
            DB.append((0,1))
        elif item == '^':
            B.append((r,c))
            DB.append((-1,0))
        elif item == 'v':
            B.append((r,c))
            DB.append((1,0))
        elif item == '.' and r==len(lines)-1:
            T = (r,c)

rmax = len(lines)-2
cmax = len(line)-2

def move_blizzards():
    for i,(dr,dc) in enumerate(DB):
        r,c = B[i]
        if (r+dr,c+dc) not in W:
            B[i]=(r+dr,c+dc)
        else:
            if dr>0:
                B[i]=(1,c)
            elif dr<0:
                B[i]=(rmax,c)
            elif dc>0:
                B[i]=(r,1)
            elif dc<0:
                B[i]=(r,cmax)
            else:
                assert False

def show(B,DB,W,Q):
    for row in range(0,rmax+2):
        toprint=''
        for column in range(0,cmax+2):
            if (row,column) in B:
                i = B.index((row,column))
                if DB[i]==(0,1):
                    toprint+='>'
                elif DB[i]==(0,-1):
                    toprint+='<'
                elif DB[i]==(1,0):
                    toprint+='v'
                elif DB[i]==(-1,0):
                    toprint+='^'
            elif (row,column) in Q:
                toprint+='o'
            elif (row,column) in W:
                toprint+='#'
            else:
                toprint+='.'
        print(toprint)

Q = deque()

Q.append(S)
minutes = 0
for _ in range(400):
    move_blizzards()

    for _ in range(len(Q)):
        next = Q.popleft()
        for dr,dc in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
            r,c = next
            rr=r+dr
            cc=c+dc

            if (rr,cc) not in B and (rr,cc) not in W and (rr,cc) not in Q and 0<=rr<=rmax+1 and 0<=cc<=cmax+1:
                assert (rr,cc) not in B
                assert (rr,cc) not in W
                Q.append((rr,cc))

    minutes+=1
    if T in Q:
        break
print('------------------------')
print('Part 1:',minutes)
print('------------------------')

S_ = S
S = T
T = S_

Q = deque()
Q.append(S)
for _ in range(400):
    move_blizzards()

    for _ in range(len(Q)):
        next = Q.popleft()
        for dr,dc in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
            r,c = next
            rr=r+dr
            cc=c+dc

            if (rr,cc) not in B and (rr,cc) not in W and (rr,cc) not in Q and 0<=rr<=rmax+1 and 0<=cc<=cmax+1:
                assert (rr,cc) not in B
                assert (rr,cc) not in W
                Q.append((rr,cc))

    minutes+=1
    if T in Q:
        break

S_ = S
S = T
T = S_

Q = deque()
Q.append(S)

for _ in range(400):
    move_blizzards()

    for _ in range(len(Q)):
        next = Q.popleft()
        for dr,dc in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
            r,c = next
            rr=r+dr
            cc=c+dc

            if (rr,cc) not in B and (rr,cc) not in W and (rr,cc) not in Q and 0<=rr<=rmax+1 and 0<=cc<=cmax+1:
                assert (rr,cc) not in B
                assert (rr,cc) not in W
                Q.append((rr,cc))

    minutes+=1
    if T in Q:
        break

print('Part 2:',minutes)
print('------------------------')