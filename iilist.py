a=[5,6,7,[8,9,[56,78],[9,1,3]]]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    sum+=a[i][j][k]
                    k=k+1
            else:
                sum+=a[i][j]
            j=j+1
    else:
        sum+=a[i]
    i=i+1
print(sum)                            


