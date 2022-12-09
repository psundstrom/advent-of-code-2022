with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

def initObject(name,type,size,parent):
    return {'name':name,
        'type':type,
        'size':size,
        'parent': parent,
        'children':[]}

def getSize(object):
    if object['type']=='file':
        return object['size']
    elif object['type']=='dir':
        if object['size'] is None:
            object['size'] = sum([getSize(x) for x in object['children']])
            return object['size']
        else:
            return object['size']

ls=False
currentDirectory='root'

files=initObject(currentDirectory,'dir',None,None)
current=files
for line in lines:
    parts = line.split()    
    if ls:
        if parts[0]=='$':
            ls=False
        else:
            if parts[0].isdigit():
                type='file'
                name=parts[1]
                size=int(parts[0])
            elif parts[0]=='dir':
                type='dir'
                name=parts[1]
                size=None
            current['children'].append(initObject(name,type,size,current))
    if parts[0]=='$' and parts[1]=='ls':
        ls=True
    if parts[0]=='$' and parts[1]=='cd':
        if parts[2]=='..':
            current=current['parent']
        elif parts[2]=='/':
            current=files
        else:
            newDirectory=parts[2]
            # current['children'].append([initObject(newDirectory,'dir',None)])
            names = [item['name'] for item in current['children']]
            current = current['children'][names.index(newDirectory)]

sizes = []

def listSizes(obj,sizes):
    if len(obj['children'])>0:
        sizes.append(getSize(obj))
        [listSizes(x,sizes) for x in obj['children']]
        
listSizes(files,sizes)


print('------------------------')

print('Part 1:',sum([x for x in sizes if x<=100000]))

print('------------------------')

total=70000000
used=getSize(files)
unused=total-used
required=30000000
needdeleted=required-unused
needdeleted

print('Part 2:',min([x for x in sizes if x>needdeleted]))

print('------------------------')