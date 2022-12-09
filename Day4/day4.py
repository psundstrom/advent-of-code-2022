import re

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

data = [[int(j) for j in re.split('\W+', line)] for line in lines]

k=0
for item in data:
    if (item[0]>=item[2] and item[1]<=item[3]) or (item[0]<=item[2] and item[1]>=item[3]):
        k=k+1

print('------------------------')
print('Part 1:',k)

k=0
for item in data:
    if (item[0]>=item[2] and item[0]<=item[3]) or (item[1]>=item[2] and item[1]<=item[3]):
        k=k+1
    elif (item[2]>=item[0] and item[2]<=item[1]) or (item[3]>=item[0] and item[3]<=item[1]):
        k=k+1

print('------------------------')
print('Part 2:',k)
print('------------------------')