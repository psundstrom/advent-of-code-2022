import numpy as np
import plotly.graph_objects as go


class Monkey:
    def __init__(self,items,operation,operationvalue,test,truetarget,falsetarget):
        self.items=items
        self.operation=operation
        self.operationvalue=operationvalue
        self.test=test
        self.truetarget=truetarget
        self.falsetarget=falsetarget
        self.activity=0

    def __str__(self):
        return f'Items: {self.items}, Activity:{self.activity}'

    def inspect_and_throw(self,allmonkeys,dividebythree=True):
        
        for item in self.items:
            item == reduce(item)
            self.activity+=1
            # Perform operation
            item = self.operation(item,self.operationvalue)
            # Divide by 3 and round down
            if dividebythree:
                item=item//3
            # Test

            # if item>1e20:
            #     item=reduce(item)
            if item%self.test==0:
                # item=item//self.test
                allmonkeys[self.truetarget].items.append(item)
            else:
                allmonkeys[self.falsetarget].items.append(item)
        self.items=[]
        

def add(old,value):
    return old+value

def multiply(old,value):
    return old*value

def square(old,value):
    return old**2

def reduce(g):
    for p in [2,3,5,7,11,13,17,19]:
        while (g//(p**8))%p==0 and g%p==0:
            g=g//p
    return g

def getmonkeys():
    testmonkeys = [
        Monkey(
            items=[79, 98],
            operation=multiply,
            operationvalue=19,
            test=23,
            truetarget=2,
            falsetarget=3
        ),
        Monkey(
            items=[54, 65, 75, 74],
            operation=add,
            operationvalue=6,
            test=19,
            truetarget=2,
            falsetarget=0
        ),
        Monkey(
            items=[79, 60, 97],
            operation=square,
            operationvalue=0,
            test=13,
            truetarget=1,
            falsetarget=3
        ),
        Monkey(
            items=[74],
            operation=add,
            operationvalue=3,
            test=17,
            truetarget=0,
            falsetarget=1
        )
    ]

    monkeys=[
        Monkey(
            items=[54, 61, 97, 63, 74],
            operation=multiply,
            operationvalue=7,
            test=17,
            truetarget=5,
            falsetarget=3
        ),
        Monkey(
            items=[61, 70, 97, 64, 99, 83, 52, 87],
            operation=add,
            operationvalue=8,
            test=2,
            truetarget=7,
            falsetarget=6
        ),
        Monkey(
            items=[60, 67, 80, 65],
            operation=multiply,
            operationvalue=13,
            test=5,
            truetarget=1,
            falsetarget=6
        ),
        Monkey(
            items=[61, 70, 76, 69, 82, 56],
            operation=add,
            operationvalue=7,
            test=3,
            truetarget=5,
            falsetarget=2
        ),
        Monkey(
            items=[79, 98],
            operation=add,
            operationvalue=2,
            test=7,
            truetarget=0,
            falsetarget=3
        ),
        Monkey(
            items=[72, 79, 55],
            operation=add,
            operationvalue=1,
            test=13,
            truetarget=2,
            falsetarget=1
        ),
        Monkey(
            items=[63],
            operation=add,
            operationvalue=4,
            test=19,
            truetarget=7,
            falsetarget=4
        ),
        Monkey(
            items=[72, 51, 93, 63, 80, 86, 81],
            operation=square,
            operationvalue=0,
            test=11,
            truetarget=0,
            falsetarget=4
        ),
    ]
    return monkeys,testmonkeys

monkeys,testmonkeys=getmonkeys()
for item in testmonkeys:
    print(item)

for i in range(20):
    for monkey in monkeys:
        monkey.inspect_and_throw(monkeys)

activity = [monkey.activity for monkey in monkeys]

activity.sort()

print('------------------------')
print('Part 1:',activity[-2]*activity[-1])
print('------------------------')

monkeys,testmonkeys=getmonkeys()

activities=[]
diffs=[]
activity=[0,0,0,0]
slope=[0,0,0,0]
r = 20
for i in range(400):
    for monkey in testmonkeys:
        monkey.inspect_and_throw(testmonkeys,dividebythree=False)
        
    if i%1==0:
        oldactivity = activity
        activity = [monkey.activity for monkey in testmonkeys]
        diff = [activity[j]-oldactivity[j] for j,_ in enumerate(activity)]
        activities.append(activity)
        diffs.append(diff)
        
        if i>r:
            slope = [(a-activities[r][j])/(i-r) for j,a in enumerate(activity)]
            print(slope)
            print([int(s*(1000-r))+activities[r][j] for j,s in enumerate(slope)])

fig = go.Figure()

for k,_ in enumerate(activities[0]):
    fig.add_trace(go.Scatter(x0=0,dx=1,y=[a[k] for a in activities]))

for k,slo in enumerate(slope):
    fig.add_trace(go.Scatter(x0=0,dx=1,y=[int((g-r)*slo)+activities[r][k] for g in range(600)]))

fig.show()

# for monkey in testmonkeys:
#     print(monkey)

# activity = [monkey.activity for monkey in testmonkeys]

# print(activity)

# print('Part 2:',activity[-2]*activity[-1])