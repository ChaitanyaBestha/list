a= [2, -7, 5, -64, -14]
i=0
b=[]
c=[]
for i in range(0,len(a)):
    if a[i]<0:
        b.append(a[i])
    else:
        c.append(a[i])   
print(b,len(b)) 
print(c,len(c))  


