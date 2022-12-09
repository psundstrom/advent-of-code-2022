print('2022 - Day 1')

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

foods=';'.join(lines)

elves = foods.split(';;')

sums = [sum([int(i) for i in j.split(';')]) for j in elves]

sums.sort()

print('------------------------')
print('Part 1:',max(sums))
print('------------------------')
print('Part 2:',sum(sums[-3:]))
print('------------------------')