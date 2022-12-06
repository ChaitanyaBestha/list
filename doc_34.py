a=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
b=[]
while i<len(a):
    if  type(a[i])!=float and type(a[i])!=str:
        b.append(a[i])
    i=i+1
print(b)        
