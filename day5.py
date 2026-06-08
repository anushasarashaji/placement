#dynamic sliding window ...that is we dont know at what particular lenth the condition will be met
"""nums=list(map(int,input().split()))
k=int(input())
l,u,sum,mx=0,0,0,0
n=len(nums)
while u<n:
    sum=sum+nums[u]
    while sum>k:
        sum=sum-list[l]
        l=l+1
    mx=max(mx,l-u+1)
    u=u+1
print(mx)
"""

#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""def maxScore(self, cardPoints: List[int], k: int) -> int:
    s = sum(cardPoints[:k])
    mx = s
    n = len(cardPoints)
    i, j = k - 1, n - 1
    while i >= 0:
        s = s - cardPoints[i] + cardPoints[j]
        mx = max(s, mx)
        i = i - 1
        j = j - 1
    return mx
"""

#password
"""pas=input()
upper=False
special=False
lower=False
digit=False
space=False
for i in pas:
    if i.isupper():
        upper=True
    elif i.islower():
        lower=True
    elif i.isdigit():
        digit=True
    elif i==" ":
        space=True
    else:
        special=True
if len(pas)>=8 and upper and lower and special and digit and not space:
    print("valid")
else:
    print("not valid")
    """

#binary search find range
#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""def searchRange(self, nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]
    first = -1
    end = -1
    l = 0
    h = len(nums) - 1
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            first = mid
            h = mid - 1
        elif target < nums[mid]:
            h = mid - 1
        else:
            l = mid + 1
    l = 0
    h = len(nums) - 1
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            end = mid
            l = mid + 1
        elif target < nums[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return [first, end]
"""

#find peak element
"""  def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == 0:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return n
        else:
            l = 1
            h = n - 1
            while l <= h:
                m = (l + h) // 2
                if nums[m - 1] < nums[m] > nums[m + 1]:
                    return m
                elif nums[m - 1] > nums[m]:
                    h = m - 1
                else:
                    l = m + 1
"""

#https://leetcode.com/problems/search-a-2d-matrix/
#binary seacrch in matrix
"""
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    row = len(matrix)
    col = len(matrix[0])
    l, h = 0, (row * col) - 1
    while l <= h:
        mid = (l + h) // 2
        i = mid // col
        j = mid % col
        if matrix[i][j] == target:
            return True
        elif target < matrix[i][j]:
            h = mid - 1
        else:
            l = mid + 1
    return False
"""

# koko banana problem (binary search problem)
# eg    3     6     7     11
# 1b/h  3     6     7     11        27hrs->np
# 2b/h  2     3     4     6         15hrs->np
# 3b/h  1     2     3     4         10hrs->np
# 4b/h  1     2     2     3         8hrs->P
# 5b/h                                   ->p
#
#
#
# 11b/h                                   ->p

"""def minEatingSpeed(self, piles: List[int], h: int) -> int:
  def can_eat(m, piles, h):
    total = 0
    for i in piles:
      total += math.ceil(i / m)
    if total > h:
      return False
    else:
      return True

  l, e = 1, max(piles)
  while l <= e:
    mid = (l + e) // 2
    if can_eat(mid, piles, h):
      e = mid - 1
    else:
      l = mid + 1
  return l
"""



str1=input()
s=""

# for i in str1:
#   if i not in d:
#     d[i]=1
#   else:
#     d[i]+=1
# for key,item in d.items():
#   s=s+key+str(item)
# print(s)
count=1
n=len(str1)
for i in range(n-1):
  if(str1[i]==str1[i+1]):
    count=count+1
  else:
    s=s+str1[i]+str(count)
    count=1
s=s+str1[n-1]+str(count)
print(s)
