'''
import csv
filename=input("Enter the name of the file:")
filename=filename+".csv"
with open(filename,'r') as f:
    reader=csv.reader(f)
    data=list(reader)
data=data[1:]
for i in len(data):
    data[0][i]=float(data[0][i])
    data[i][
        
data=list(map(float,data))
print(data)
'''
t=int(input("Enter number of points "))
print("Enter x y in new line ")
l=[]
g=[]
for i in range(0,t):
    x=[]
    r=[]
    z=[]
    x=[float(y) for y in input().split()]
    r.append(x)
    l.append(r)
    z.append("P"+str(i+1))
    g.append(z)
print(l)
d=0
print(len(l))
while(len(l)!=1):
    mi=10000000
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            for i1 in range(i+1,len(l)):
                for j1 in range(0,len(l[i])):
                    euc=((l[i][j][0]-l[i1][j1][0])*(l[i][j][0]-l[i1][j1][0]))+((l[i][j][1]-l[i1][j1][1])*(l[i][j][1]-l[i1][j1][1]))
                    print(euc)
                    if(euc<mi):
                        mii1=i1
                        mii=i
                        mi=euc
    x1=l[mii]+l[mii1]
    naming=g[mii]+g[mii1]
    del g[mii]
    del g[mii1-1]
    del l[mii]
    del l[mii1-1]
    g.append(naming)
    l.append(x1)
    print(g)
