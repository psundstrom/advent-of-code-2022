import sys

filename = sys.argv[1] if len(sys.argv)>1 else 'input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

C=[]
for line in lines:
    words=line.split()
    C.append([(int(words[6]),0,0,0),(int(words[12]),0,0,0),(int(words[18]),int(words[21]),0,0),(int(words[27]),0,int(words[30]),0)])

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

def get_geodes(end,robots,resources,costs,minutes,maxgeodes):
    if minutes>=end:
        return resources[3]
    ttn = time_to_next(robots,resources,costs)
    if robots[3]*(end-minutes+1)+resources[3]+sum(range(end-minutes))<maxgeodes:
        return -1
    minutes+=1
    resources=[rc+r for rc,r in zip(resources,robots)]
    for i,t in reversed(list(enumerate(ttn))):
        if t+minutes<=end and (i==3 or robots[i]<max([c[i] for c in costs])):
            newrobots=robots.copy()
            newrobots[i]+=1
            newresources=[r-c+rb*t for r,c,rb in zip(resources,costs[i],robots)]
            maxgeodes = max(maxgeodes,get_geodes(end,newrobots,newresources,costs,minutes+t,maxgeodes))
                
    return max(maxgeodes,resources[3]+robots[3]*max(end-minutes,0))
    
robots=[1,0,0,0]
resources=[0,0,0,0]
ans=0
for i,costs in enumerate(C):
    ge = get_geodes(24,robots,resources,costs,0,0)
    print(i+1,ge)
    ans+=(i+1)*ge

print('------------------------')
print('Part 1:',ans)
print('------------------------')

robots=[1,0,0,0]
resources=[0,0,0,0]
ans = 1
for i,costs in enumerate(C[0:3]):
    ge = get_geodes(32,robots,resources,costs,0,0)
    print(i+1,ge)
    ans*=ge

print('Part 2:',ans)
print('------------------------')