a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max=0
min=1000
for i in range(0,len(a)):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i] 
print((len(max),max))
print((len(min),min))         