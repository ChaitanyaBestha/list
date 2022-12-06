a=["ChaiTaNya"]
i=0
b=[]
while i<len(a):
    j=0 
    while j<len(a[i]):
        if a[i][j].isupper():
            b.append(a[i][j])
        j=j+1
    i=i+1
print(b)        