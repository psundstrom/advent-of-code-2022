# orecost=4
# claycost=2
# obsidiancost=(3,14)
# geodecost=(2,7)
from time import sleep
from copy import deepcopy

costs=[(2,0,0,0),(3,0,0,0),(3,8,0,0),(3,0,12,0)]

costs=[(4,0,0,0),(2,0,0,0),(3,14,0,0),(3,0,7,0)]

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

print(get_purchases([4+2+3+3,14,7,0],costs))
print(next_geode([1,1,1,0],[0,0,0,0],costs))
print(next_obsidian([1,1,0,0],[0,0,0,0],costs))

print(time_to_next([1,1,0,0],[10,10,0,0],costs))

print(time_to_next([4, 6, 2, 2],[7, 39, 2, 1],costs))

# assert False

# if robots = [1,0,0,0] (only ore)
#     wait g minutes and buy ore
#     wait y minutes and buy clay

# if robots = [1,1,0,0] (only ore and clay)
#     wait x minutes and buy clay
#     wait y minutes and buy obsidian

# if robots = [1,1,1,0] 
#     wait x minutes and buy clay
#     wait y minutes and buy obsidian
#     wait z minutes and buy geode

# if robots = [1,1,1,1]
#     wait x minutes and buy clay
#     wait y minutes and buy obsidian
#     wait z minutes and buy geode

SEEN={}
def get_geodes(robots,resources,costs,minutes,maxgeodes):
    end=24
    # print(minutes)
    if minutes>=end:
        print(robots)
        return resources[3]
    ttn = time_to_next(robots,resources,costs)
    if robots[3]>0 and ttn[3]+minutes>end and resources[3]+robots[3]*(end-minutes)<=maxgeodes:
        print('pruned 1',robots,resources,minutes,maxgeodes,ttn)
        return -1
    if robots[2]>0 and robots[3]==0 and ttn[3]+minutes>end:
        print('pruned 2',robots,resources,minutes,maxgeodes,ttn)
        return -1
    if robots[1]>0 and robots[2]==0 and ttn[2]+minutes>end:
        print('pruned 3',robots,resources,minutes,maxgeodes,ttn)
        return -1
    minutes+=1
    resources=[rc+r for rc,r in zip(resources,robots)]
    for i,t in reversed(list(enumerate(ttn))):
        if t+minutes<end:
            newrobots=robots.copy()
            newrobots[i]+=1
            newresources=[r-c+rb*t for r,c,rb in zip(resources,costs[i],robots)]
            maxgeodes = max(maxgeodes,get_geodes(newrobots,newresources,costs,minutes+t,maxgeodes))

    print(robots,resources,max(maxgeodes,resources[3]+robots[3]*max(end-minutes,0)),minutes)
    return max(maxgeodes,resources[3]+robots[3]*max(end-minutes,0))
# def get_geodes(robots,resources,costs,minutes,maxgeodes):
#     end = 24
#     # print(minutes)
#     # # print(robots)
#     # print(resources[3])
#     # print(next_obsidian(robots,resources,costs))
#     if robots[2]==0 and next_obsidian(robots,resources,costs)+minutes>end:
#         return -1
#     if robots[3]==0 and robots[2]>0 and next_geode(robots,resources,costs)+minutes>end:
#         return -1
#     if next_obsidian(robots,resources,costs)>0 and next_geode([r+d for r,d in zip(robots,[0,0,1,0])],resources,costs)>0 and robots[3]==0 and robots[2]==0 and next_obsidian(robots,resources,costs) + next_geode([r+d for r,d in zip(robots,[0,0,1,0])],resources,costs)+minutes>end:
#         # print('prune')
#         return -1
#     if next_geode(robots,resources,costs)>0 and (robots[3]+1)*(end-minutes-next_geode(robots,resources,costs))+resources[3]<=maxgeodes: # and next_geode(robots,resources,costs)+minutes>24:
#         #assert False
#         return -1
#     if robots[3]>0 and next_geode(robots,resources,costs)+minutes>24 and robots[3]*(end-minutes)<maxgeodes:
#         return -1
#     if minutes==end:
#         # print(robots)
#         # print(resources)
#         if robots[3]>0:
#             print(resources)
#         return resources[3]
    
#     purchases = get_purchases(resources,costs)
#     # print(purchases)
#     minutes+=1
#     resources=[rc+r for rc,r in zip(resources,robots)]
#     # maxgeodes=0
#     for i in range(len(purchases)-1,-1,-1):
#         if purchases[i]>1:
#             # print('Buy',i)
#             newrobots=robots.copy()
#             newrobots[i]+=1
#             newresources=[r-c for r,c in zip(resources,costs[i])]
#             maxgeodes=max(maxgeodes,get_geodes(newrobots,newresources,costs,minutes,maxgeodes))
#     return max(maxgeodes,get_geodes(robots,resources,costs,minutes,maxgeodes))
  
robots=[1,0,0,0]
print(get_geodes(robots,resources,costs,0,-2))