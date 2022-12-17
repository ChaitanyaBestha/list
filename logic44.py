a=[8,4,3,2,5]
i=0
b=[]
while i<len(a)-1:
    c=str(a[i])+str(a[i+1])
    b.append(int(c))
    i=i+1
print(b) 
