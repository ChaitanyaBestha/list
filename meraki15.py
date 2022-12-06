# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# a=int(input("enter no:"))
# b=[]
# while i<len(n):
#     j=0
#     while j<len(n):
#         if n[i]+n[j]==a:
#             c=[n[i],n[j]]
#             if c not in b:
#                 b.append(c)
#         j=j+1
#     i=i+1
# print(b)
            
num=30
n=[10,11,12,13,14,17,18,19]
i=0
while i<len(n):
    j=i+1
    while j<len(n):
        if n[i]+n[j]==num:
            print(list((n[i],n[j])),end=" ")
        j=j+1
    i=i+1