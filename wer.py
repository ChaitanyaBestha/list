# a=[4,1,2,3,5]
# a.append(9)
# print(a)

# a=[2,4,5,8,7,2]
# i=0
# even=0
# odd=0
# while i<len(a):
#     if a[i]%2==0:
#         even=even+1
#     else:
#         odd=odd+1
#     i=i+1
# print(even,"even")
# print(odd,"odd")            

# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# i=0
# c=[]
# while i<len(a):
#     d=a[i]*b[i]
#     c.append(d)
#     i=i+1
# print(c) 
# max=0
# i=0
# while i<len(c):
#     if c[i]>max:
#         max=c[i]
#     i=i+1
# print(max)          
    
# a=[[11,2,3],[4,5,6],[8,9,12]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     max=0
#     while j<len(a[i]):
#         if a[i][j]>max:
#             max=a[i][j]
#         j=j+1
#     b.append(max)
#     i=i+1
# print(b)        
# a=[11,30,50]
# i=0
# c=""
# while i<len(a):
#     c=c+str(a[i])
#     i=i+1
# print(c) 
#    
# a=[1,2,3,4]
# b=[1,2,3,4]
# a[0]=9
# b[0]=5
# print(a)
# print(b)
a=[1,2,3,4,5,6,7,8,9,10]
i=1
c=0
d=len(a)
while i<len(a):
    # j=0
    # c=0
    # while j<=i:
    if i%a[i]==0:
        c=c+1
        # j=j+1
if c==2:
    print(i,end=" ")
    i=i+1            

