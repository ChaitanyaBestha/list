# a=[12, 67, 98, 34]
# i=0
# b=[]
# while i<len(a):
#     sum=0
#     while a[i]>0:
#         c=a[i]%10
#         sum=sum+c
#         a[i]=a[i]//10
#     b.append(sum)
#     i=i+1
# print(b)        

a=[12,67,98,32]  
i=0
c=[]
while i<len(a):
    b=a[i]
    sum=0
    while b>0:
        r=b%10
        sum=sum+r
        b=b//10
    c.append(sum)
    i=i+1
print(c)



    
