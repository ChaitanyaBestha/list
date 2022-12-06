a=[1,2,3,4,5,6]
b=[]
i=0
j=-1
while i<len(a)-3:
    c=a[j],a[i]
    b.append(list(c))
    i=i+1
    j=j-1
print(b)    
