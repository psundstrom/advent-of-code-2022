# orecost=4
# claycost=2
# obsidiancost=(3,14)
# geodecost=(2,7)

orecost=2
claycost=3
obsidiancost=(3,8)
geodecost=(3,12)

costs=[(2,0,0,0),(3,0,0,0),(0,3,8,0),(0,3,0,12)]

robots = [1,0,0,0]

resources=[0,0,0,0]

minutes=0

def get_purchases(resources,costs):

    return [min([r//c for r,c in zip(resources,cost) if c>0]) for cost in costs]

def get_geodes(robots,resources,costs,minutes):
    if minutes==24:
        return resources,resources__
    while True:
        p = get_purchases(resources,costs)
        print(p)
        minutes+=1
        resources=[rc+r for rc,r in zip(resources,robots)]
        for i,item in enumerate(p):
            resources__ = [0,0,0,0]
            if p[i]>0:
                newrobots=[r+rp for r,rp in zip(robots,[1 if j==i else 0 for j in range(0,4)])]
                newresources=[r-c for r,c in zip(resources,costs[i])]
                resources_ = get_geodes(newrobots,newresources,costs,minutes)
                if resources_[3]>resources__[3]:
                    resources__=resources_
        resources_ = get_geodes(robots,resources,costs,minutes)
        if resources_[3]>resources__[3]:
            return resources_
        else:
            return resources__

print(get_geodes(robots,resources,costs,0))
