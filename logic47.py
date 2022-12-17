a=[(1,2),(3,4),(1,2),(5,6),(7,8),(1,2),(3,4),(3,4),(7,8),(9,10)]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)
    

