#left rotation optimal
"""nums=list(map(int,input().split()))
k=int(input())
n=len(nums)
if k>=n:
    k=k%n
j=k-1
for i in range(k//2):
    nums[i],nums[j]=nums[j],nums[i]
    j=j-1
j=n-1
for i in range(k,k+(n-k)//2):
    nums[i],nums[j]=nums[j],nums[i]
    j=j-1
j=n-1
for i in range(n//2):
    nums[i],nums[j]=nums[j],nums[i]
    j=j-1
print(nums)
"""
#right rotion optimal
"""nums=list(map(int,input().split()))
k=int(input())
n=len(nums)
if k>=n:
    k=k%n
j=k
for i in range(k//2+1):
    nums[i],nums[j]=nums[j],nums[i]
    j=j-1
    print(nums)
j=n-1
for i in range(k+1,k+(n-k)//2):
    nums[i],nums[j]=nums[j],nums[i]
    j=j-1
    print(nums)
j=n-1
for i in range(n//2):
    nums[i],nums[j]=nums[j],nums[i]
    j=j-1
print(nums)
"""
#rotion using function (more simple)
"""nums=list(map(int,input().split()))
k=int(input())
n=len(nums)
k=k%n
def reverse(nums,i,j):
    while i<j:
        nums[i],nums[j]=nums[j],nums[i];
        i=i+1
        j=j-1

if k==0:
    print(nums)
else:
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    reverse(nums,0,n-1)
    print(nums)
"""

"""l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
i,j=0,0
while(i<len(l1) and j<len(l2)):
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i=i+1
    else:
        l3.append(l2[j])
        j=j+1
while i<len(l1):
    l3.append(l1[i])
    i=i+1
while j<len(l2):
    l3.append(l2[j])
    j=j+1
print(l3)
"""

"""s=input()
str2=""
flag=0
for i in s:
    if i.isalnum():
        str2=str2+i
n=len(str2)
print(str2)
j=n-1
for i in range(n//2):
    if str2[i]!=str2[j]:
        flag=1
        break
    else:
        i+=1
        j-=1
if flag==0:
    print(True)
else:
    print(False)
    """

"""books=list(map(int,input().split()))
k=int(input())
n=len(books)
s=books[0]+books[1]+books[2]
mx=s
for i in range(1,n-k+1):
    s=s-books[i-1]+books[i+k-1]
    mx=max(mx,s)

print(mx)"""


def isUgly(self, n: int) -> bool:
    if n <= 0:
        return False
    for i in [2, 3, 5]:
        while n % i == 0:
            n = n // i
    return n == 1

