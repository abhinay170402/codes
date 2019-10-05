t=int(input())
for i in range(t):
    n,x,y=list(map(int,input().split()))
    if(n%4==0):
        print(x,y)
    elif(n%4==1):
        print(-y,x)
    elif(n%4==2):
        print(-x,-y)
    else:
        print(y,-x)
