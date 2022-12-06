binary=[1,0,1]
a=len(binary)
i=-1
k=0
sum=0
while i>=-a:
    c=binary[i]*2**k
    sum=sum+c
    i=i-1
    k=k+1
print(sum)
