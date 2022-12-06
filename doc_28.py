# a=[1,1,2,3,4,5,1,2]
# b=[]
# i=0
# while i<len(a):
#     num=a[i]
#     if num==a[i] and num!=1:
#         b.append(a[i])
#     i=i+1
# print(b)
a=[1,1,2,3,4,5,1,2]
b=[]
n=int(input("enter which number you want remove:"))
i=0
while i<len(a):
    if a[i]!=n:
        b.append(a[i])
    i=i+1
print(b)                