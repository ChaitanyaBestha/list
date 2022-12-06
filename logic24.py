a="my name is chaitu"
i=0
c=""
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]==" ":
            c=c+"-"
        else:
            c=c+a[i][j]
        j=j+1
    i=i+1
print('"'+c+'"')                

