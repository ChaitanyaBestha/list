# a=[2,34,45,32,6,76,87,89,4,1]
# min1=1000
# min2=1000
# min3=1000
# i=0
# while i<len(a):
#     if a[i]<min1:
#         min1=a[i]
#     i=i+1
# j=0
# while j<len(a):
#     if a[j]<min2 and a[j]!=min1:
#         min2=a[j] 
#     j=j+1
# k=0
# while k<len(a):
#     if a[k]<min3 and a[k]!=min2 and a[k]!=min1:
#         min3=a[k]
#     k=k+1
# print(min1)
# print(min2)
# print(min3)                       

a=[2,34,45,32,6,76,87,89,4,1]
min1=1000
min2=1000
max1=0
max2=0# min3=1000
i=0
while i<len(a):
    if a[i]<min1:
        min1=a[i]
    i=i+1
j=0
while j<len(a):
    if a[j]<min2 and a[j]!=min1:
        min2=a[j] 
    j=j+1
# k=0
# while k<len(a):
#     if a[k]<min3 and a[k]!=min2 and a[k]!=min1:
#         min3=a[k]
#     k=k+1
# print(min1)
# print(min2)
# # print(min3)
# a=[2,34,45,32,6,76,87,89,4,1]
# max1=0
# max2=0
# max3=0
i=0
while i<len(a):
    if a[i]>max1:
        max1=a[i]
    i=i+1
j=0
while j<len(a):
    if a[j]>max2 and a[j]!=max1:
        max2=a[j] 
    j=j+1
# k=0
# while k<len(a):
#     if a[k]>max3 and a[k]!=max2 and a[k]!=max1:
#         max3=a[k]
#     k=k+1
# print(max1)
print(max2)
# print(min1)
print(min2)
# print(max3)                                              