# orecost=4
# claycost=2
# obsidiancost=(3,14)
# geodecost=(2,7)
from time import sleep
from copy import deepcopy

costs=[(2,0,0,0),(3,0,0,0),(3,8,0,0),(3,0,12,0)]

robots = [1,0,0,0]

resources=[0,0,0,0]

minutes=0

def get_purchases(resources,costs):
    return [min([r//c for r,c in zip(resources,cost) if c>0]) for cost in costs]

def next_obsidian(robots,resources,costs):
    if robots[0]>0 and robots[1]>0:
        return max([(rc-c)//r for r,c,rc in zip(robots,costs[2],resources) if c>0])
    else:
        return 0

def next_geode(robots,resources,costs):
    if robots[0]>0 and robots[2]>0:
        return max([(rc-c)//r for r,c,rc in zip(robots,costs[3],resources) if c>0])
    else:
        return 0

def get_geodes(robots,resources,costs,minutes,maxgeodes):
    print(minutes)
    # print(robots)
    print(resources[3])
    # print(next_obsidian(robots,resources,costs))
    if robots[2]==0 and next_obsidian(robots,resources,costs)+minutes>24:
        return -1
    if robots[3]==0 and next_geode(robots,resources,costs)+minutes>24:
        return -1
    if (robots[3]+1)*(24-minutes)+resources[3]<=maxgeodes: # and next_geode(robots,resources,costs)+minutes>24:
        #assert False
        return -1
    if minutes==24:
        return resources[3]
    
    purchases = get_purchases(resources,costs)
    # print(purchases)
    minutes+=1
    resources=[rc+r for rc,r in zip(resources,robots)]
    # maxgeodes=0
    for i in range(len(purchases)-1,-1,-1):
        if purchases[i]>1:
            print('Purchase',i)
            newrobots=robots.copy()
            newrobots[i]+=1
            newresources=[r-c for r,c in zip(resources,costs[i])]
            maxgeodes=max(maxgeodes,get_geodes(newrobots,newresources,costs,minutes,maxgeodes))
    return max(maxgeodes,get_geodes(robots,resources,costs,minutes,maxgeodes))

print(get_geodes(robots,resources,costs,0,3))