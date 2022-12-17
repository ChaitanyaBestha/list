a=['red','orange','blue','green','white']
b=['black','yellow','green','blue']
i=0
c=[]
d=[]
while i<len(a):
    if a[i] not in b:
        c.append(a[i])
    elif b[i] not in a:
        d.append(b[i])
    i=i+1
print(c)
print(d)
