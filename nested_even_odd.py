a=[[2,3,4,5,6]]
b=[]
i=0
while i<len(a):
    c=a[i]
    j=0
    sum_even=0
    sum_odd=0
    while j<len(c):
        if c[j]%2==0:
            sum_even=sum_even+c[j]
        if c[j]%2!=0:
            sum_odd=sum_odd+c[j]    
        j=j+1
    b.append(sum_even)
    b.append(sum_odd)
    i=i+1
print(b) 
   

