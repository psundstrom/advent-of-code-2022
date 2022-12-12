import timeit

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

map=[[] for c in range(len(lines))]

for i,line in enumerate(lines):
    map[i]=[c for c in line]


for i,item in enumerate(map):
    for j,item2 in enumerate(item):
        if item2=='S':
            source=(i,j)
            map[i][j]='`'
        if item2=='E':
            target=(i,j)
            map[i][j]='{'

def print_map(shortestpaths,map,source=None,target=None,filename=None):
    if filename is not None:
        f = open(filename, "w")
    for i,row in enumerate(shortestpaths):
        toprint = [str(shortestpaths[i][j]).ljust(5) if shortestpaths[i][j]<1e300 else '  '+map[i][j]+'  ' for j,column in enumerate(row)]
        if target[0]==i:
            toprint[target[1]]='E'
        if source[0]==i:
            toprint[source[1]]='S'
        if filename is None:
            print(''.join(toprint))
        else:
            f.write(''.join(toprint)+'\n')
    if filename is not None:
        f.close()

# printMap(shortestpaths)

def get_unvisited(visited,shortestpaths,target=None):
    unvisited=[]
    distances=[]
    disttotarget=[]
    for i,_ in enumerate(visited):
        for j,value in enumerate(visited[i]):
            if not value and shortestpaths[i][j]<1e300:
                unvisited.append((i,j))
                distances.append(shortestpaths[i][j])
                if target is not None:
                    disttotarget.append(abs(i-target[0])+abs(j-target[1]))
    if target is None: # order by tentative distance
        return [x for _, x in sorted(zip(distances, unvisited))]
    else: # order by distance to target
        return [x for _, x in sorted(zip(disttotarget, unvisited))]

def find_ways(starti,startj,shortestpaths,visited):
    # ways=[]
    for i in [starti-1,starti+1]:
        if i >=0 and i < len(shortestpaths) and not visited[i][startj]:
            dist = ord(map[i][startj])-ord(map[starti][startj])
            if dist<=1:
                # ways.append((i,startj))
                path = shortestpaths[starti][startj]+1
                currentpath = shortestpaths[i][startj]
                if path<currentpath:
                    shortestpaths[i][startj]=path
    for j in [startj-1,startj+1]:
        if j>=0 and j < len(shortestpaths[0]) and not visited[starti][j]:
            dist = ord(map[starti][j])-ord(map[starti][startj])
            if dist<=1:
                # ways.append((starti,j))            
                path = shortestpaths[starti][startj]+1
                currentpath = shortestpaths[starti][j]
                if path<currentpath:
                    shortestpaths[starti][j]=path
    visited[starti][startj]=True
    return shortestpaths,visited

def find_shortest_path(map,source,target,max=None):
    shortestpaths=[[1e300 for b in map[0]] for c in map]

    visited=[[False for b in map[0]] for c in map]

    shortestpaths[source[0]][source[1]]=0
    unvisited=get_unvisited(visited,shortestpaths)

    while not visited[target[0]][target[1]] and len(unvisited)>0:
        if max is not None and shortestpaths[unvisited[0][0]][unvisited[0][1]]>max:
            # if current shortest is larger than max, no shorter paths available
            return 1e300,shortestpaths
        shortestpaths,visited=find_ways(*unvisited[0],shortestpaths,visited)
        unvisited = get_unvisited(visited,shortestpaths)
    
    return shortestpaths[target[0]][target[1]],shortestpaths

part1,shortestpaths = find_shortest_path(map,source,target)

print('------------------------')
print('Part 1:',part1)
print('------------------------')

starts=[]
best = int(1e300)
for i,row in enumerate(map):
    for j,_ in enumerate(row):
        if map[i][j]=='a':
            shortestsofar,_ = find_shortest_path(map,(i,j),target,best)
            if shortestsofar<best:
                best=shortestsofar

print('Part 2:',best)
print('------------------------')