n=int(input("enter no:"))
a=n
for i in range(0,n):
    h=n%10000
    b=n%1000
    c=n%100
    d=n%10
    i=i+1
print(n-h,"+",h-b,"+",b-c,"+",c-d,"+",d)    
