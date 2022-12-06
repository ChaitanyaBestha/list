a=["jyo","chaitu"]
b=[]
i=0
while i>-len(a):
    d=a[i]
    j=-1
    r=""
    while j>=-len(d):
        r+=d[j]
        j=j-1
    i=i-1
    b.append(r) 
print(b)       
