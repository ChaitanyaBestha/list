a=[[2,3,4],[6,8,9,10],[4,96]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        c=a[i][j]
        b.append(c)
        j=j+1
    i=i+1    
print(b)      
