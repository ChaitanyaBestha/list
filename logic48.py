a=[(1,2),(3,4),(1,2),(5,6),(7,8),(1,2),(3,4),(3,4),(7,8),(9,10)]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j] not in b:
            b.append(a[i][j])
        j=j+1
    i=i+1
print(b)
