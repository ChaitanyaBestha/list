a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        # j=j+1   
    b.append(sum)
    i=i+1
print(b)
