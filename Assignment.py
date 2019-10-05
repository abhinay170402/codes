t=int(input())
for i in range(t):
    n,x=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l.sort()
    s=0
    for j in range(x):
        s=s+l[j]
    print(s)
        
