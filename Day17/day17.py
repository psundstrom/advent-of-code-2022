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


rocks = set([(0,y) for y in range(0,7)])

def push(dir,rock,rocks):
    tentative = [(x,y+dir) for x,y in rock]
    if max([y for _,y in tentative])>6 or min([y for _,y in tentative])<0 or any([t in rocks for t in tentative]):
        return rock
    else:
        return tentative

j=0
prevmax=0
for i in range(2022):
    rock = get_rock(i%5,max([x for x,y in rocks])+4)

    settled=False
    while not settled:
        dir = -1 if pushes[j%len(pushes)]=='<' else 1
        j+=1
        rock = push(dir,rock,rocks)
        tentative = [(x-1,y) for x,y in rock]
        # print(rock,tentative)
        if any([t in rocks for t in tentative]):
            # print('Settled',rock)
            rocks.update(set(rock))
            settled=True
        else:
            rock = tentative

    prevmax=max([x for x,y in rocks])

print('------------------------')
print('Part 1:',max([x for x,y in rocks]))
print('------------------------')

for x in range(prevmax,prevmax-20,-1):
    toprint=''
    for y in range(7):
        if (x,y) in rocks:
            toprint+='#'
        else:
            toprint+='.'
    print(toprint)