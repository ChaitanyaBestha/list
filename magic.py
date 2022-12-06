a=[[2,9,4],
   [17,5,3],
   [6,1,8]]
i=0
while i<len(a):
    j=0
    row=0
    column=0
    while j<len(a):
        row=row+a[i][j]
        column=column+a[i][j]
        m=0
        while m<len(a):
            n=0
            di2=0
            di1=0
            while n<len(a):
                di2=di2+a[m][n]
                di1=di1+a[m][n]
                n=n+1
            m=m+1
        j=j+1
    i=i+1   
print(column)
print(row)
print(di2)           
if row==column==di2==di1:
    print("magic")
else:
    print("not")            
