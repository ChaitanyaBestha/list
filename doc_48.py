a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
b=[]
i=0
while i<len(a):
    c=a[i],a[i+1],a[i+2]
    b.append(list(c))
    i=i+3
print(b)    