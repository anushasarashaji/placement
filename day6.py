# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#recursion

# def fun(n):
#     if n==0:
#         return
#     print(n)
#     fun(n-1)
#
# def fun2(n):
#     if n==0:
#         return 200
#     x=fun2(n-1)
#     print(n)
#     return x
#
# n=5
#
# m=fun2(n)
# print(m)


# 5 4 3 2 1 2 3 4 5
# def fun(n):
#     if n==0:
#         return
#     #if n%2==0:
#     print(n,end=" ")
#     fun(n-1)
#     if n>1:
#         print(n,end=" ")
# n=10
# fun(n)


#1 2 3 4 5 4 3 2 1

# def fun(n,m=0):
#     if n==m:
#         return
#     print(m+1,end=" ")
#     fun(n,m+1)
#     if m+1!=5:
#         print(m+1,end=" ")
# n=5
# fun(n)


#min number of steps
# def reduce(n):
#     if n==1:
#         return 0
#     elif n%2==0:
#         return 1+reduce(n//2)
#     else:
#         return 1+min(reduce(n-1),reduce(n+1))
# n=15
# print(reduce(n))


# def wildfire(grid,i,j):
#     if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
#         return
#     grid[i][j]=2
#     wildfire(grid,i+1,j)
#     wildfire(grid,i-1,j)
#     wildfire(grid,i,j+1)
#     wildfire(grid,i,j-1)
#
# matrix=[[1,1,1,1],[1,0,0,0],[0,0,1,1],[0,1,0,0]]
# wildfire(matrix,0,0)
# count=0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==1:
#             count+=1
# print(count)

#https://leetcode.com/problems/flood-fill/
# def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#     def ff(image, i, j, org, color):
#         if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != org:
#             return
#         image[i][j] = color
#         ff(image, i + 1, j, org, color)
#         ff(image, i - 1, j, org, color)
#         ff(image, i, j + 1, org, color)
#         ff(image, i, j - 1, org, color)
#
#     org = image[sr][sc]
#     if org != color:
#         ff(image, sr, sc, org, color)
#     return image

#https://leetcode.com/problems/number-of-islands/
# def numIslands(self, grid: List[List[str]]) -> int:
#     if not grid:
#         return 0
#
#     def island(grid, i, j):
#
#         if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
#             return
#         grid[i][j] = '2'
#         island(grid, i + 1, j)
#         island(grid, i - 1, j)
#         island(grid, i, j + 1)
#         island(grid, i, j - 1)
#
#     count = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 island(grid, i, j)
#                 count += 1
#     return count

#backtracking another method where path has to be printed so not all
# def maze(grid,path,i,j,n):
#     if i==n and j==n:
#         print(path)
#         return
#     if i+1<=n and grid[i+1][j]==1:
#         maze(grid,path+'D',i+1,j,n)
#     if j+1<=n and grid[i][j+1]==1:
#         maze(grid,path+'R',i,j+1,n)
#
# grid=[[1,1,0,1],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
# n=len(grid)
# maze(grid,"",0,0,n-1)
