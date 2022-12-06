a= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
c=[]
while i<len(a):
    b=a.count(a[i])
    if b>=1:
        d=[a[i],b]
        if d not in c:
            c.append(d)
    i=i+1
print(c)
