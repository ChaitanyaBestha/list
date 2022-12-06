a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
b=[]
while i<len(a):
    c=a[i]
    j=0
    d=[]
    while j<len(c):
        d.append(c[j])
        j=j+1
    b.append(d)
    i=i+1
print(b)
    