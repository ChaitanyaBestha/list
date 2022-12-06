a=[5,6,7[8,9,[5,6,7,8],[9,1,3]]]
i=0
sum=0
while i<len(a):
    j=0
    sum1=0
    while j<len(a[i]):
        sum1=sum1+a[i][j]
        j=j+1
    sum=sum+sum1
    i=i+1
print(sum)    

