a=[8,9,10,3]
b=[9,10]
c=[]
i=0
while i<len(a):
    if a[i] not in b:
        c.append(a[i])
    i=i+1 
print(c)       



