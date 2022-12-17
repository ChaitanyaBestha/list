a='chaitanya'
i=0
c=[]
while i<len(a):
    b=a.count(a[i])
    if a[i] not in c:
        c.append(a[i])
        print(a[i]+str(b),end="")
        
    i=i+1
