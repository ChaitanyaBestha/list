a = [50, 40, 23, 70, 56, 12, 5, 10, 7]
b=[]
i=0
while i<len(a):
    if a[i]>=20 and a[i]<=40:
        b.append(a[i])
    i=i+1
print(len(b))        
