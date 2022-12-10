with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

instructions = [()]*len(lines)
for i,line in enumerate(lines):
    parts = line.split()
    instructions[i]=(parts[0],int(parts[1]) if len(parts)>1 else 0)

cycle = 0
register = [1]

for item in instructions:
    if item[0]=='noop':
        cycle=cycle+1
        register.append(register[cycle-1])
    elif item[0]=='addx':
        cycle=cycle+1
        register.append(register[cycle-1])
        cycle=cycle+1
        register.append(register[cycle-1]+item[1])

def get_strength(register,cycle):
    return register[cycle-1]*cycle

print('------------------------')
print('Part 1:',sum([get_strength(register,cycle) for cycle in [20, 60, 100, 140, 180, 220]]))
print('------------------------')

screen=['']*240

for i,item in enumerate(register[:-1]):
    sprite = item
    if i%40<=(item+1) and i%40>=(item-1):
        screen[i]='#'
    else:
        screen[i]='.'

print(''.join(screen[0:40]))
print(''.join(screen[40:80]))
print(''.join(screen[80:120]))
print(''.join(screen[120:160]))
print(''.join(screen[160:200]))
print(''.join(screen[200:240]))

print('------------------------')

