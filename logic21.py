a=[2,7,8,4,5]
b=[]
i=0
j=1
while i<len(a):
    c=a[i]*j
    d=c%10
    b.append(d)
    i=i+1
    j=j+1
print(b)    