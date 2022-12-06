a=int(input("num"))
i=1
count=0
while i<=a:
    if a%i==0:
        count=count+1
    i=i+1
if count==2:
#     print("prime")
# else:
#     print("not")    
    j=0
    while a>0:
        b=a%10
        j=j*10+b
        a=a//10
    c=0
    k=1
    while k<=j:
        if j%k==0:
            c=c+1
        k=k+1
    if c==2:
        print("twisted prime num")
    else:
        print("not")

else:
    print("no")