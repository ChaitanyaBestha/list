a=[[1 ,2, 3],
   [4, 5, 6],
   [9, 8, 9]] 
# i=0
# r=2
# m=0
# while i<len(a):
#     j=2
#     while j<len(a):
#         m=m+a[i][r]
#         j=j+1
#         r=r-1
#     i=i+1
# print(m)    
# i=0
# p=2
# n=0
# while i<len(a):
#     j=2
#     while j<len(a):
#         n=n+a[i][r]
#         j=j+1
#         p=p-1
#     i=i+1
# print(n) 
i=0
p=0
n=0
while i<len(a):
    j=0
    while j<len(a):
        n=n+a[i][p]
        j=j+1
        p=p+1
    i=i+1
print(n)        



