a=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[j][i]
        j=j+1   
    b.append(sum) 
    i=i+1
print(b)




    