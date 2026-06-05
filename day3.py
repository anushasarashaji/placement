#leetcode 66
"""def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits ) -1 ,-1 ,-1):
        if digits[i ]= =9:
            digits[i ] =0
        else:
            digits[i ] =digits[i ] +1
            return digits
    return [1 ] +digits
"""

#https://leetcode.com/problems/single-number/
"""
def singleNumber(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            sum=sum^i
        return sum
"""

#https://leetcode.com/problems/missing-number/
"""def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        for i in range(n):
            if nums[i]!=i:
                return i
        return i+1"""

"""def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumn=(n(n+1))//2
        suml=sum(nums)
        mis=sumn-suml
        if(mis>0):
            return mis
        else:
            return 0
                """

#https://leetcode.com/problems/power-of-two/
""" def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        while n:
            if n==1:
                return True
            elif n%2!=0:
                return False
            else:
                n=n//2"""
#optimal
"""def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        if n&(n-1)==0:
            return True
        else:
            return False"""
"""
nums=list(map(int,input))
n=len(nums)
i=0
while i<=n-1:
    if i==n-1:
        return True
    else:
        steps=nums[i]
        i=i+steps
"""

"""nums=list(map(int,input().split()))
max,sec=0,0
for p in nums:
    if p>max:
        sec=max
        max=p
    elif p>sec and p!=max:
        sec=p
print(sec)
"""

"""num=list(map(int,input().split()))
count,max=0,0
for i in num:
    for j in num:
        if i==j:
            count=count+1
    if count>max:
        max=i
print(max)
"""

"""d={}
nums=list(map(int,input().split()))
max,sec=0,0
for i in nums:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for key,value in d.items():
    if value>max:
        sec=max
        max=key
print(sec)
print(max)
"""

"""d={}
age=list(map(int,input().split()))
vote=list(map(int,input().split()))
n=len(age)
for i in range(n):
    if vote[i] not in d and age[i]>=18:
        d[vote[i]]=1
    elif age[i]>=18:
        d[vote[i]]+=1
max,sec=0,0
for i in d:
    if d[i]>=max:
        sec=max
        max=d[i]
if sec==max:
    print(-1)
else:
    print(max)
"""


#reverse a list without using function(two pointer)
"""nums=list(map(int,input().split()))
n=len(nums)
j=n-1
for i in range(n//2):
    nums[i],nums[j]=nums[j],nums[i]
    j=j-1
print(nums)
"""

#half reverse optimal
"""nums=list(map(int,input().split()))
n=len(nums)
j=n//2-1
for i in range(n//4):
    nums[i],nums[j]=nums[j],nums[i]
    j=j-1
print(nums)"""

#left rotion brute force
"""nums=list(map(int,input().split()))
t=int(input())
n=len(nums)
while t>0:
    a=nums[0]
    for i in range(1,n,1):
        nums[i-1]=nums[i]
    nums[n-1]=a
    print(nums)
    t=t-1
"""
#right rotation brute force
"""nums=list(map(int,input().split()))
t=int(input())
n=len(nums)
while t>0:
    a=nums[n-1]
    for i in range(n-1,0,-1):
        nums[i]=nums[i-1]
    nums[0]=a
    print(nums)
    t=t-1
"""
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