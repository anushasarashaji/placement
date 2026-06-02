

#l=list(map(int,input().split()))
"""l=input().split()
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
"""

"""l=list(map(int,input().split()))
l2=[]

for i in l:
    if i not in l2:
        if l.count(i)%2!=0:
            l2.append(i)
print(l2)
"""

"""l1=list(map(int,input().split()))
l1.sort()
res=[]
for i in l1:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i) # it adds in descending order
print(res)
"""

"""n=int(input())
l=list(map(int,input().split()))
nop=0
count=0
for i in l:
    if i>0:
        nop+=i
    elif nop>0 and i==-1:
        nop=nop-1
    elif nop==0 and i==-1:
        count=count+1
print(count)
"""


def lemonadeChange(self, bills: List[int]) -> bool:
    five, ten = 0, 0
    for coin in bills:
        if coin == 5:
            five = five + 1
        elif coin == 10:
            if five > 0:
                five = five - 1
                ten = ten + 1
            else:
                return False
        else:
            if five > 0 and ten > 0:
                five = five - 1
                ten = ten - 1
            elif five >= 3:
                five = five - 3
            else:
                return False
    return True
