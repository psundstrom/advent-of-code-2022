import math

global M

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
            self.activity+=1
            # Perform operation
            item = self.operation(item,self.operationvalue,not dividebythree)
            # Divide by 3 and round down
            if dividebythree:
                item=item//3
            if item%self.test==0:
                allmonkeys[self.truetarget].items.append(item)
            else:
                allmonkeys[self.falsetarget].items.append(item)
        self.items=[]

def getM(monkeys):
    res = 1
    for item in [monkey.test for monkey in monkeys]:
        res*=item
    return res

def add(old,value,optimize):
    new = old+value
    return new

def multiply(old,value,optimize):
    return old*value

def square(old,value,optimize):
    if optimize:
        return M+(old**2)%M
    else:
        return old**2

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


for i in range(20):
    M = getM(monkeys)
    for monkey in monkeys:
        monkey.inspect_and_throw(monkeys)

activity = [monkey.activity for monkey in monkeys]

activity.sort()

print('------------------------')
print('Part 1:',activity[-2]*activity[-1])
print('------------------------')

monkeys,testmonkeys=getmonkeys()

for i in range(10000):
    for monkey in monkeys:
        monkey.inspect_and_throw(monkeys,dividebythree=False)

activity = [monkey.activity for monkey in monkeys]

activity.sort()

print('Part 2:',activity[-2]*activity[-1])
print('------------------------')