C=set()
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    words = line.split(',')
    C.add((int(words[0]),int(words[1]),int(words[2])))

def check(cube,pocket=set()):
    n=6
    t=0
    for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        if (cube[0]+d[0],cube[1]+d[1],cube[2]+d[2]) in C or (cube[0]+d[0],cube[1]+d[1],cube[2]+d[2]) in pocket:
            n-=1
    return n

def expand_air_pocket(start):
    stillsearching=True
    pocket = set()
    toexplore = []
    toexplore.append(start)
    while stillsearching:
        cube=toexplore.pop()
        pocket.add(cube)
        for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            test = (cube[0]+d[0],cube[1]+d[1],cube[2]+d[2])
            if test[0]==21 or test[0]==0 or test[1]==21 or test[1]==0 or test[2]==21 or test[2]==0:
                return set()
            if test not in C and test not in pocket:
                toexplore.append(test)
        if len(toexplore)==0:
            stillsearching=False
    return pocket

n=0
tested = set()
nair=0
pocket=set()
for cube in C:
    n+=check(cube)
    for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        test = (cube[0]+d[0],cube[1]+d[1],cube[2]+d[2])
        if test not in C and test not in pocket:
            pocket.update(expand_air_pocket(test))

print('------------------------')
print('Part 1:',n)
print('------------------------')

n2=0
for cube in C:
    n2+=check(cube,pocket)

print('Part 2:',n2)
print('------------------------')
