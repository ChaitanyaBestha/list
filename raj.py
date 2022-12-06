# a=[[2,3,4],[4,7,9],[8,9,10]]
# i=0
# sum1=0
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[j][i]
#         j=j+1
#     sum1=sum1+sum    
#     i=i+1
# print(sum1)
# a='chaitanya'
# i=0
# c=[]
# while i<len(a):
#     b=a.count(a[i])
#     if b>=1:
#         d=[a[i],b]
#         if d not in c:
#             c.append(d)
#     else:
#         c.append(a[i])
#     i=i+1
# print(c)
# a=[1,2,3,4,5,6]
# i=-1
# b=[]
# while i>=-len(a):
#     b.append(a[i])
#     i=i-1
# print(b)    

# a=[8,4,3,2,5]
# i=0
# b=[]
# while i<len(a)-1:
#     c=str(a[i])+str(a[i+1])
#     b.append(int(c))
#     i=i+1
# print(b) 

# a=['rajitha','thanvi','chaitanya']
# i=0
# while i<len(a):
#     c=a[i][-1]
#     print(c,end=" ")
#     i=i+1   

a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
i=0
b=[]
while i<len(a):
    c=(a[i],a[i+1],a[i+2])
    b.append(list(c))
    i=i+3
print(b)    
m