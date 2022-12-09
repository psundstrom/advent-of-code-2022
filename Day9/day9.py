import numpy as np

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

moves=[]
for line in lines:
    g = line.split()
    moves.append([g[0],int(g[1])])

def takeStep(dd,head,tail):
    head = head + dd
    dist = head - tail
    if max(abs(dist))>1:
        tail = tail+np.array([x/max(1,abs(x)) for x in dist])
    return head, tail

def catchup(head,tail):
    dist = head - tail
    if max(abs(dist))>1:
        tail = tail+np.array([x/max(1,abs(x)) for x in dist])
    return tail

def direction(d):
    if d=='L':
        return [0,-1]
    elif d=='R':
        return [0,1]
    elif d=='U':
        return [1,0]
    elif d=='D':
        return [-1,0]
    else:
        print('Unknown direction:',d)
        return [0,0]

head = np.array([0,0])
tail = np.array([0,0])
tailpositions = []
for item in moves:
        for i in range(item[1]):
                head,tail = takeStep(direction(item[0]),head,tail)
                tailpositions.append(tail.tolist())

unique = []

for item in tailpositions:
    if item not in unique:
        unique.append(item)

print('------------------------')
print('Part 1:',len(unique))

head = np.array([0,0])
tails = np.array([np.array([0,0]) for i in range(9)])
tailpositions = []
for item in moves:
    for i in range(item[1]):
        d=direction(item[0])
        head,tails[0] = takeStep(d,head,tails[0])
        for j in range(1,len(tails)):
            tails[j] = catchup(tails[j-1],tails[j])
        
        tailpositions.append(tails[-1].tolist())

unique=[]
for item in tailpositions:
    if item not in unique:
        unique.append(item)

print('------------------------')
print('Part 2:',len(unique))
print('------------------------')