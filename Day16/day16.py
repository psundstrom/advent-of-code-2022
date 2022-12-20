from collections import deque
import networkx as nx
from itertools import combinations


with open('Day16/input.txt') as file:
    lines = [line.strip() for line in file]

V={}
opened_=[]

G = nx.DiGraph()

for line in lines:
    words = line.split()
    valve = words[1]
    flowrate = int(words[4].split('=')[-1][:-1])
    tunnels = ''.join(line.split(';')[-1].split()[4:]).split(',')
    V[valve]=[flowrate,tunnels]
    for tunnel in tunnels:
        G.add_edge(valve,tunnel)
    opened_.append(flowrate==0)

def find_shortest_path(V,source,target):
    return nx.shortest_path_length(G,source,target)

opened = [k for i,k in enumerate(V.keys()) if opened_[i]]
unopened = [k for i,k in enumerate(V.keys()) if not opened_[i]]

shortestpaths={}
for valve1 in unopened+['AA']:
    shortestpaths[valve1]={}
    for valve2 in unopened:
        shortestpaths[valve1][valve2]=find_shortest_path(V,valve1,valve2)
print('paths found')
n = 0
def get_pressure(start,pressure,minutes,unopened,oldmax=0,opened=[]):
    global n
    n+=1
    if pressure+sum([V[valve][0]*(minutes-shortestpaths[start][valve]) for valve in unopened])<oldmax:
        return 0
    if minutes<=min([shortestpaths[start][valve] for valve in unopened]):
        return pressure
    else:
        if start in unopened:
            unopened.remove(start)
            opened.append(start)
            minutes-=1
            pressure+=V[start][0]*minutes
        if len(unopened)==0:
            return pressure

        pr=[]
        for valve in unopened:
            if len(pr)>0:
                maxpr=max(pr)
            else:
                maxpr=0
            pr.append(get_pressure(valve,pressure,minutes-shortestpaths[start][valve],unopened.copy(),maxpr,opened.copy()))
        return max(pr)

uo = unopened.copy()
max1 = get_pressure('AA',0,30,uo)

print('------------------------')
print('Part 1:',max1)
print('------------------------')

max2=max1
for i in range(1,len(unopened)):
    print(i)
    for valves in combinations(unopened,i):
        unopened_ = unopened.copy()
        for item in valves:
            unopened_.remove(item)
        v1 = get_pressure('AA',0,26,unopened_)
        v2 = get_pressure('AA',0,26,list(valves),max2-v1)
        if v1+v2>max2:
            max2=v1+v2

print('Part 1:',max2)
print('------------------------')