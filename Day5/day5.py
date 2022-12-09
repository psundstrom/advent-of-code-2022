with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

def get_stacks(lines):
    stacks=[[] for i in range(9)]

    for line in lines:
        for i,item in enumerate(line):
            if line==['']:
                break
            if item.isupper():
                ind = i//4
                stacks[ind].append(item)

    for item in stacks:
        item.reverse()
    
    return stacks


instructions=[]
for line in lines:
    g = line.split()
    if len(g)>0 and g[0]=='move':
        instructions.append([int(g[1]),int(g[3]),int(g[5])])

def move1(n,fr,to,stacks):
    # print('Move',n,'from',fr,'to',to)
    for i in range(n):
        if len(stacks[fr-1])>0:
            m = stacks[fr-1].pop()
            stacks[to-1].append(m)

stacks = get_stacks(lines)
for item in instructions:
    try:
    #    print(*item)
        move1(*item,stacks)
    except:
        print(item)
        raise Exception

print('------------------------')
print('Part 1:',''.join([i[-1] for i in stacks]))

def move2(n,fr,to,stacks):
    # print('Move',n,'from',fr,'to',to)
    tomove = stacks[fr-1][-n:]
    del stacks[fr-1][-n:]
    for item in tomove:
        stacks[to-1].append(item)

stacks = get_stacks(lines)
for item in instructions:
    try:
    #    print(*item)
        move2(*item,stacks)
    except:
        print(item)
        raise Exception

print('------------------------')
print('Part 2:',''.join([i[-1] for i in stacks]))
print('------------------------')