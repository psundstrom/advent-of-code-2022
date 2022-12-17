f = open("input.txt", "r")
data = f.read()
f.close()

pairs=[]
for item in data.split('\n\n'):
    pairs.append([eval(x) for x in item.split('\n')])

def compare(p1,p2):
    if type(p1)==int:
        p1=[p1]
    if type(p2)==int:
        p2=[p2]
    if len(p1)==1 and len(p2)==1 and type(p1[0])!=list and type(p2[0])!=list:
        if p1[0]==p2[0]:
            return None
        else:
            return p1[0]<p2[0]
    elif len(p1)==1 and len(p2)==1:
        if type(p1[0])==list:
            p1=p1[0]
        if type(p2[0])==list:
            p2=p2[0]
        return compare(p1,p2)
    else:
        if type(p1)==int:
            p1=[p1]
        if type(p2)==int:
            p2=[p2]
        for i,item in enumerate(p1):
            if i>(len(p2)-1):
                return False
            elif p1[i]!=p2[i]:
                res = compare(p1[i],p2[i])
                if res is not None:
                    return res
                else:
                    continue 
        if len(p1)<len(p2):
            return True

def bubblesort(packets):
    sorting=True
    while sorting:
        sorting=False
        for i in range(len(packets)-1):
            if not compare(packets[i],packets[i+1]):
                packets[i],packets[i+1]=packets[i+1],packets[i]
                sorting=True
    return packets

correct=[]
for i,item in enumerate(pairs):
    if compare(*item):
        correct.append(i+1)

print('------------------------')
print('Part 1:',sum(correct))
print('------------------------')

packets = [item for sublist in pairs for item in sublist]

packets.append([[2]])
packets.append([[6]])

sortedpackets = bubblesort(packets)

i1=sortedpackets.index([[2]])+1
i2=sortedpackets.index([[6]])+1

print('Part 2:',i1*i2)
print('------------------------')