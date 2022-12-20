class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

    def shift(self,n):
        if n==0:
            return
        nabs = abs(n)
        d = -1 if n<0 else 1
        for _ in range(nabs):
            if d==-1:
                self.moveleft()
            else:
                self.moveright()

    def insertafter(self,node):
        node.prev = self
        self.next.prev = node
        node.next = self.next
        self.next=node

    def moveright(self):
        next = self.next
        prev = self.prev
        self.prev = next
        self.next = next.next
        next.next.prev = self
        next.next = self
        next.prev = prev
        prev.next = next
    
    def moveleft(self):
        next = self.next
        prev = self.prev
        self.prev = prev.prev
        self.next = prev
        prev.prev.next = self
        prev.prev = self
        prev.next = next
        next.prev = prev

    def getneighbour(self,n):
        if n>0:
            neighbour = self.next
            for i in range(n-1):
                neighbour=neighbour.next
            return neighbour
        elif n<0:
            neighbour = self.prev
            for i in range(abs(n)-1):
                neighbour=neighbour.prev
            return neighbour
        else:
            return self

    def findvalue(self,value):
        current=self.next
        while current.data!=value:
            current=current.next
        return current

def get_data(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    original = []
    for i,line in enumerate(lines):
        this = Node(data=int(line))
        if i>0:
            this.prev = original[i-1]
            original[i-1].next= this
        original.append(this)
        if this.data==0:
            zero=this

    original[0].prev=original[-1]
    original[-1].next=original[0]

    return original,zero

original,zero = get_data('input.txt')

length = len(original)

for item in original:
    item.shift(item.data%(length-1))

print('------------------------')
print('Part 1:',zero.getneighbour(1000).data+zero.getneighbour(2000).data+zero.getneighbour(3000).data)
print('------------------------')

part2,zero = get_data('input.txt')

for item in part2:
    item.data*=811589153

for _ in range(10):
    for item in part2:
        item.shift(item.data%(length-1))

print('Part 2:',zero.getneighbour(1000).data+zero.getneighbour(2000).data+zero.getneighbour(3000).data)
print('------------------------')