import numpy as np

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

trees = []
for line in lines:
    trees.append([int(i) for i in line])

trees = np.array(trees)

def findRange(tree,view):
    n=0
    for item in view:
        if item<tree:
            n=n+1
        else:
            n=n+1
            break
    return n

def totalRange(x,y,trees):
    c = trees[x,y]
    n1 = findRange(c,np.flip(trees[x,:y]))
    n2 = findRange(c,trees[x,y+1:])
    n3 = findRange(c,np.flip(trees[:x,y]))
    n4 = findRange(c,trees[x+1:,y])

    return n1*n2*n3*n4

def isVisible(x,y,trees):
    c = trees[x,y]
    b1 = all(c>trees[x,:y]) or len(trees[x,:y])==0
    b2 = all(c>trees[x,y+1:]) or len(trees[x,y+1:])==0
    b3 = all(c>trees[:x,y]) or len(trees[:x,y])==0
    b4 = all(c>trees[x+1:,y]) or len(trees[x+1:,y])==0

    return b1 or b2 or b3 or b4

n = 0
for x,item in enumerate(trees):
    for y,item2 in enumerate(item):
        if isVisible(x,y,trees):
            n=n+1
print('------------------------')
print('Part 1:',n)

ranges = []
for x,item in enumerate(trees):
    for y,item2 in enumerate(item):
        ranges.append(totalRange(x,y,trees))

print('------------------------')
print('Part 2',max(ranges))
print('------------------------')