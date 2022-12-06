a=[[8,3,4],[9,6,0],[2,4,9,8]]
b=[]
i=0
while i<len(a):
    c=a[i]
    j=0
    sum=0
    while j<len(c):
        sum=sum+c[j]
        j=j+1
    b.append([sum])
    i=i+1
print(b)    



