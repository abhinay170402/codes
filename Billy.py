t=int(input())
for i in range(t):
    n=int(input())
    c=[]
    p=[]
    a=[]
    for j in range(n):
        x,y=list(map(str,input().split()))
        c.append(x)
        p.append(y)
    for k in range(n):
        if(c[k]=='captured' and len(a)<6):
            a.append(p[k])
        elif(c[k]=='withdraw' and len(a)<6):
            a.append(p[k])
        elif(c[k]=='deposit'):
            a.remove(p[k])
    for z in a:
        print(z)
        
