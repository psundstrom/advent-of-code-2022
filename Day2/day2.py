def shape_score(shape):
    if shape in ['A','X']:
        return 1
    elif shape in ['B','Y']:
        return 2
    elif shape in ['C','Z']:
        return 3
    else:
        return -1000

def get_move(shape,result):
    if result=='Y':
        return shape
    elif result=='X':
        if shape=='A':
            return 'C'
        elif shape=='B':
            return 'A'
        elif shape=='C':
            return 'B'
        else:
            return ''        
    elif result=='Z':
        if shape=='A':
            return 'B'
        elif shape=='B':
            return 'C'
        elif shape=='C':
            return 'A'
        else:
            return ''

def match_score(shape1,shape2):
    score=-1000
    if shape_score(shape2)==1:
        if shape_score(shape1)==1:
            score=3
        elif shape_score(shape1)==2:
            score=0
        elif shape_score(shape1)==3:
            score=6
    elif shape_score(shape2)==2:
        if shape_score(shape1)==1:
            score=6
        elif shape_score(shape1)==2:
            score=3
        elif shape_score(shape1)==3:
            score=0
    elif shape_score(shape2)==3:
        if shape_score(shape1)==1:
            score=0
        elif shape_score(shape1)==2:
            score=6
        elif shape_score(shape1)==3:
            score=3
    return score+shape_score(shape2)

with open('input.txt') as file:
    lines = [line.rstrip().split() for line in file]

scores1 = [match_score(*item) for item in lines]
scores2 = [match_score(item[0],get_move(*item)) for item in lines]

print('------------------------')
print('Part 1:',sum(scores1))
print('------------------------')
print('Part 2:',sum(scores2))
print('------------------------')