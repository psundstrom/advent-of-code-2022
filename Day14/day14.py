def get_rocks(filename='input.txt'):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    rocks=set()
    for line in lines:
        words=[r.strip() for r in line.split('->')]
        for i in range(1,len(words)):
            start = (*[int(b) for b in words[i-1].split(',')],)
            end = (*[int(b) for b in words[i].split(',')],)
            add_rock(start,end,rocks)
    ymax=max([y for x,y in rocks])
    return rocks,ymax

def add_rock(start,end,rocks):
    rock = list(start)

    rocks.add((*rock,))

    while (abs(end[0]-rock[0])+abs(end[1]-rock[1]))>0:
        diff = ((((end[0]-rock[0])//max(abs(end[0]-rock[0]),1)),(end[1]-rock[1])//max(abs(end[1]-rock[1]),1)))
        rock[0]+=diff[0]
        rock[1]+=diff[1]
        rocks.add((*rock,))

def print_map(xstart,xend,maxy,rocks):
    for x in range(xstart,xend):
        toprint=''
        for y in range(0,maxy):
            if (x,y) in rocks:
                toprint+='#'
            else:
                toprint+='.'
        print(toprint)

def sand1(x,y,maxy,rocks):
    while y<maxy:
        if (x,y+1) not in rocks:
            y+=1
        elif (x-1,y+1) not in rocks:
            x-=1
            y+=1
        elif (x+1,y+1) not in rocks:
            x+=1
            y+=1
        else:
            return x,y
    return (-1,-1)

def sand2(x,y,maxy,rocks):
    while y<maxy:
        if (x,y+1) not in rocks and y+1<maxy:
            y+=1
        elif (x-1,y+1) not in rocks and y+1<maxy:
            x-=1
            y+=1  
        elif (x+1,y+1) not in rocks and y+1<maxy:
            x+=1
            y+=1
        else:
            return x,y
    return (-1,-1)

rocks,ymax = get_rocks()
n = 0
res = (1,1)
while res!=(-1,-1):
    res = sand1(500,0,ymax,rocks)
    if res!=(-1,-1):
        n+=1
        rocks.add(res)
print('------------------------')
print('Part 1:',n)
print('------------------------')

rocks,ymax=get_rocks()

n=0
while (500,0) not in rocks:
    res = sand2(500,0,ymax+2,rocks)
    if (500,0) not in rocks:
        rocks.add(res)
        n+=1

print('Part 2:',n)
print('------------------------')