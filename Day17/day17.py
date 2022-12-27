from collections import deque

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

pushes = lines[0]

def get_rock(i,offset):
    if i==0:
        return [(0+offset,2),(0+offset,3),(0+offset,4),(0+offset,5)]
    elif i==1:
        return [(1+offset,2),(0+offset,3),(1+offset,3),(2+offset,3),(1+offset,4)]
    elif i==2:
        return [(0+offset,2),(0+offset,3),(0+offset,4),(1+offset,4),(2+offset,4)]
    elif i==3:
        return [(0+offset,2),(1+offset,2),(2+offset,2),(3+offset,2)]
    elif i==4:
        return [(0+offset,2),(1+offset,2),(0+offset,3),(1+offset,3)]
    else:
        assert False


rocks = deque([(0,y) for y in range(0,7)])

def push(dir,rock,rocks):
    tentative = [(x,y+dir) for x,y in rock]
    if max([y for _,y in tentative])>6 or min([y for _,y in tentative])<0 or any([t in rocks for t in tentative]):
        return rock
    else:
        return tentative

i=0
j=0
rocks = deque([(0,y) for y in range(0,7)])

# Manually found, based on j%10091 (length of input)
cyclestart=1688 # start of first cycle
heightstart=2645 # height at start of first cycle
cycle=1690 # length of cycle
heightcycle=2647 # added each cycle
L=1000000000000

while i<1000000000000:
    if i==2022:
        print('------------------------')
        print('Part 1:',max([x for x,y in rocks]))
        print('------------------------')

    rock = get_rock(i%5,max([x for x,y in rocks])+4)

    settled=False
    while not settled:
        if j%(10091)==0 and j>0 and i>2022:
            i=L-(L-cyclestart)%cycle
            maxoffset = max([x for x,y in rocks])
        dir = -1 if pushes[j%len(pushes)]=='<' else 1
        j+=1
        rock = push(dir,rock,rocks)
        tentative = [(x-1,y) for x,y in rock]
        if any([t in rocks for t in tentative]):
            rocks.extend(rock)
            settled=True
        else:
            rock = tentative
    i+=1

    # Significant speedup by purging unneeded rocks
    if len(rocks)>500:
        while len(rocks)>500:
            rocks.popleft()

print('------------------------')
print('Part 2:',max([x for x,y in rocks])-maxoffset+heightstart+((i-cyclestart)//cycle)*heightcycle)
print('------------------------')