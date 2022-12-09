with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

def getPriority(s):
    if s.isupper():
        return ord(s)-38
    else:
        return ord(s)-96

def findTheThing(lines):
    for item in set(lines[0]):
        if item in lines[1] and item in lines[2]:
            return item

p = ['']*len(lines)

for i,line in enumerate(lines):
    str1 = line[0:int(len(line)/2)]
    str2 = line[int(len(line)/2):]
    for c in str1:
        if c in str2:
            p[i]=c

print('------------------------')
print('Part 1:',sum([getPriority(j) for j in p]))

g = ['']*int(len(lines)/3)
j = 0
for i in range(0,len(lines),3):
    g[j]=findTheThing(lines[i:i+3])
    j=j+1

print('------------------------')
print('Part 2:',sum([getPriority(h) for h in g]))
print('------------------------')
