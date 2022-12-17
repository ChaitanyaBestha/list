a=['a','b','a','a','d','c','c','f']
i=0
j=1
b=''
while i<len(a):
    c=a[i]+a[j]
    b=b+c
    i=i+3
    j=j+3
print(b)