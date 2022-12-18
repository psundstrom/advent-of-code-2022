from collections import deque
import networkx as nx


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

for key in V.keys():
    print(key,V[key][0])

def find_shortest_path(V,source,target):
    return nx.shortest_path_length(G,source,target)
    # Q = deque()
    # visited = set()
    # visited.add(source)
    # Q.append(source)
    # dist = dict.fromkeys(V.keys())
    # for item in dist.keys():
    #     dist[item]=0

    # while len(Q)>0:
    #     v = Q.pop()
    #     if v == target:
    #         return dist[v]
    #     for pot in V[v][1]:
    #         if pot not in visited:
    #             dist[pot]=dist[v]+1
    #             visited.add(pot)
    #             Q.append(pot)



opened = [k for i,k in enumerate(V.keys()) if opened_[i]]
unopened = [k for i,k in enumerate(V.keys()) if not opened_[i]]

print(opened)
print(unopened)
print(len(unopened))

n = 0
def get_pressure(start,pressure,minutes,unopened,opened=[]):
    global n
    n+=1
    if minutes<=0:
        return pressure
    else:
        if start in unopened:
            unopened.remove(start)
            opened.append(start)
            minutes-=1
            pressure+=V[start][0]*minutes
        if len(unopened)==0:
            return pressure
        return max([get_pressure(valve,pressure,minutes-find_shortest_path(V,start,valve),unopened.copy(),opened.copy()) for valve in unopened])

uo = unopened.copy()
print(get_pressure('AA',0,30,uo))
print(n)

print([(find_shortest_path(V,'AA',v)) for v in V.keys()])
print([nx.shortest_path_length(G,'AA',v) for v in V.keys()])