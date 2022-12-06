a=[71,85,"chaitu",58,17]
b=[]
i=0
while i<len(a):
    if type(a[i])==str:
        d=a[i]
        k=d[::-1]
        b.append(k)
    else:
        y=a[i]
        b.append((y))
    i=i+1
print(b)           


