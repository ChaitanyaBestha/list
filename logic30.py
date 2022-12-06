a=[[1,3,12],[2,5],[10,9,7,6,5,17]]
i=0
b=[]
r=[]
max=len(a[0])
while i<len(a):
    j=0
    sum1=0
    c=0
    while j<len(a[i]):
        sum1=sum1+a[i][j]
        j=j+1
        c=c+1
    b.append(sum1)    
    if c>max:
        max=c
        k=max,a[i]
        r.append(list(k))
    i=i+1
print(b)
print(r)           