a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[]
i=0
j=1
while i<len(a)-1:
    c=a[j]-a[i]
    b.append(c)
    # print(b,end=" ")
    i=i+1
    j=j+1
print(b)    
# a=[2,4,6,8,10]
# b=[]
# i=0
# j=1
# while i<len(a)-1:
#     b=a[j]-a[i]
#     print(b,end=" ")
#     i=i+1
#     j=j+1


