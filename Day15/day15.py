with open('input.txt') as file:
    lines = [line.strip() for line in file]

def is_within_distance(s,b,max_distance):
    if abs(s[0]-b[0])+abs(s[1]-b[1])<=max_distance:
        return True
    return False

def get_distance(s,b):
    return abs(s[0]-b[0])+abs(s[1]-b[1])

S=[]
B=[]
for line in lines:
    words = line.split()
    sensor = (int(words[2].split('=')[-1][:-1]),int(words[3].split('=')[-1][:-1]))
    beacon = (int(words[8].split('=')[-1][:-1]),int(words[9].split('=')[-1]))    
    S.append(sensor)
    B.append(beacon)

D = [get_distance(sensor,beacon) for sensor,beacon in zip(S,B)]

y=2000000

n=0
P=set()
for s,d in zip(S,D):
    if abs(s[1]-y)>d:
        continue
    for x in range(s[0]-d+1,s[0]+d+1):
        if is_within_distance((x,y),s,d):
            if (x,y) not in B:
                P.add((x,y))

print('------------------------')
print('Part 1:',len(P))
print('------------------------')

# Find sensors with gap 1 between their regions
P=set()
for s1 in S:
    for s2 in [s for s in S if s!=s1]:
        reldis = get_distance(s1,s2)
        ranges = D[S.index(s1)]+D[S.index(s2)]
        if reldis==ranges+2:
            P.add(s1)
            P.add(s2)

# Connect the pairs
P_=[]
for s1 in P:
    for s2 in [s for s in P if s!=s1]:
        reldis = get_distance(s1,s2)
        ranges = D[S.index(s1)]+D[S.index(s2)]
        if reldis==ranges+2:
            P_.append((s1,s2))

# First pair, search along diagonal between points
s1,s2 = P_[0]
dd=[0,0]
if s1[1]<s2[1]:
    d1 = D[S.index(s1)]
    d2 = D[S.index(s2)]
    if abs(get_distance((s1[0],s1[1]+d1),s2)-d2)==2:
        search=(s1[0],s1[1]+d1+1)
        dd[1]=-1
if s1[1]>s2[1]:
    d1 = D[S.index(s1)]
    d2 = D[S.index(s2)]
    if abs(get_distance((s1[0],s1[1]-d1),s2)-d2)==2:
        search=(s1[0],s1[1]-d1-1)
        dd[1]=1
dd[0]=1 if s1[0]<s2[0] else 0

while any([is_within_distance(search,s,D[S.index(s)]) for s in P]) and dd[0]*s1[0]<=dd[0]*search[0]<=dd[0]*s2[0]:
    search=(search[0]+dd[0],search[1]+dd[1])

print('Part 2:',search[0]*4000000+search[1])
print('------------------------')
