t=int(input())
for i in range(t):
    n=int(input())
    s=[]
    for j in range(n):
        a=input()
        x=list(a)
        if(x[0]=='*'):
            x.remove('*')
            a=''.join(x)
            #print(a)
            s.pop()
        s.append(a)
    for k in range(len(s)):
        print(s[k])
