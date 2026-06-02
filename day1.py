# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#watermelon problem codeforces 4a
#https://codeforces.com/problemset/problem/4/A
"""w=int(input())
if w%2!=0 or w==2:
    print("no")
else:
    print("yes")

    x=w//2
    if x%2==0:
        print(x,x)
    else:
        print(x-1,x+1)

"""
#https://codeforces.com/problemset/problem/617/A
"""d=int(input())
if d<=5:
    print(1)
elif d%5==0:
    print(d%5)
else:
    print(d//5+1)
"""

#https://codeforces.com/problemset/problem/791/A
"""a,b=map(int,input().split())
c=0
while(a<=b):
    a=a*3
    b=b*2
    c=c+1
print(c)
"""

n,m,a,b=map(int,input().split())
tn=n*a
tm=n//m
c=n-tm*m
cb=min(b,c*a)
tt=cb+tm*b
if(tn<tt):
    print(tn)
else:
    print(tt)


n,m,a,b=map(int,input().split())
if a*m<b:
    print(a*n)
else:
    print(((n//m)*b)+min(b,(n%m)*a))