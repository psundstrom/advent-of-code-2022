import sys

filename = sys.argv[1] if len(sys.argv)>1 else 'input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

def get_decimal(snafu):
    digits = list(snafu)
    ans=0
    p = 1
    while len(digits)>0:
        digit = digits.pop(-1)
        if digit=='=':
            k=-2
        elif digit=='-':
            k=-1
        else:
            k=int(digit)
        ans+=k*p
        p*=5
    return ans

def get_snafu(decimal):
    digits=[]
    i=20
    while i>0:
        if decimal//(5**i):
            break
        i-=1
    k=0

    p=i
    while p >= 0:
        for k in [-2,-1,0,1,2]:
            if abs(decimal-k*5**p)<sum([2*5**p_ for p_ in range(0,p)]):
                digits.append(k)
                decimal-=k*5**p
                break
        p-=1
    digits.append(decimal)

    snafu=''
    for d in digits:
        if d==-2:
            snafu+='='
        elif d==-1:
            snafu+='-'
        else:
            snafu+=str(d)
    return snafu

print('Part 1:',get_snafu(sum([get_decimal(line) for line in lines])))

