a=[1,4,1,8,2,7,1,2,1,4,8,9]
i=0
c=[]
while i<len(a):
    b=a.count(a[i])
    if b>=2:
        d=[a[i],a[i]]
        if d not in c:
            c.append(d)
    i=i+1
print(c,len(c))
