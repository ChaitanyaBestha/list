a='chaitanya'
i=0
c=[]
while i<len(a):
    b=a.count(a[i])
    if b>=1:
        d=[a[i],b]
        if d not in c:
            c.append(d)
    else:
        c.append(a[i])
    i=i+1
print(c)