# orecost=4
# claycost=2
# obsidiancost=(3,14)
# geodecost=(2,7)
from time import sleep
from copy import deepcopy

import sys

filename = sys.argv[1] if len(sys.argv)>1 else 'input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

C=[]
for line in lines:
    words=line.split()
    C.append([(int(words[6]),0,0,0),(int(words[12]),0,0,0),(int(words[18]),int(words[21]),0,0),(int(words[27]),0,int(words[30]),0)])

costs=[(2,0,0,0),(3,0,0,0),(3,8,0,0),(3,0,12,0)]

# costs=[(4,0,0,0),(2,0,0,0),(3,14,0,0),(3,0,7,0)]

# costs=[(4,0,0,0),(4,0,0,0),(4,9,0,0),(3,0,9,0)]

robots = [1,0,0,0]

resources=[0,0,0,0]

minutes=0

def get_purchases(resources,costs):
    return [min([r//c for r,c in zip(resources,cost) if c>0]) for cost in costs]

def next_obsidian(robots,resources,costs):
    if robots[0]>0 and robots[1]>0:
        return max([(c-rc)//r for r,c,rc in zip(robots,costs[2],resources) if c>0])
    else:
        return 0

def next_geode(robots,resources,costs):
    if robots[0]>0 and robots[2]>0:
        return max([(c-rc)//r for r,c,rc in zip(robots,costs[3],resources) if c>0])
    else:
        return 0

def time_to_next(robots,resources,costs):
    return [max([max(0,-((c-rc)//(-r))) if r>0 else 1000 for r,c,rc in zip(robots,costs[i],resources) if c>0]) for i in range(len(costs))]

print(time_to_next([1,1,0,0],[10,10,0,0],costs))
print(time_to_next([4, 6, 2, 2],[7, 39, 2, 1],costs))

def get_geodes(end,robots,resources,costs,minutes,maxgeodes):
    # end=24
    # print(minutes)
    if minutes>=end:
        # print(robots)
        return resources[3]
    ttn = time_to_next(robots,resources,costs)
    if robots[3] in [0] and end-minutes<maxgeodes:
        # print('pruned 0',robots,resources,minutes,maxgeodes,ttn)
        return -1
    # if robots[3]>0 and ttn[3]+minutes>end and resources[3]+robots[3]*(end-minutes)<=maxgeodes:
    #     # print('pruned 1',robots,resources,minutes,maxgeodes,ttn)
    #     return -1
    # if robots[2]>0 and robots[3]==0 and ttn[3]+minutes>end:
    #     # print('pruned 2',robots,resources,minutes,maxgeodes,ttn)
    #     return -1
    # if robots[1]>0 and robots[2]==0 and ttn[2]+minutes>end:
    #     # print('pruned 3',robots,resources,minutes,maxgeodes,ttn)
    #     return -1
    minutes+=1
    resources=[rc+r for rc,r in zip(resources,robots)]
    for i,t in reversed(list(enumerate(ttn))):
        if t+minutes<=end:
            newrobots=robots.copy()
            newrobots[i]+=1
            newresources=[r-c+rb*t for r,c,rb in zip(resources,costs[i],robots)]
            om = maxgeodes
            maxgeodes = max(maxgeodes,get_geodes(end,newrobots,newresources,costs,minutes+t,maxgeodes))
            if maxgeodes>om:
                print(robots,ttn,resources,max(maxgeodes,resources[3]+robots[3]*max(end-minutes,0)),minutes)
                
    return max(maxgeodes,resources[3]+robots[3]*max(end-minutes,0))

  

# print(get_geodes(24,robots,resources,costs,0,0))
    
robots=[1,0,0,0]
ans=0
for i,costs in enumerate(C):
    ge = get_geodes(24,robots,resources,costs,0,0)
    ans+=(i+1)*ge
    print(i+1,ge)
  
print('Part 1:',ans)

robots=[1,0,0,0]
# for i,costs in enumerate(C[0:3]):
#     print(i+1,get_geodes(32,robots,resources,costs,0,0))

#9936 is too low