# a= [2, -7, 5, -64, -14]
# i=0
# p=0
# n=0
# while i<len(a):
#     if a[i]<0:
#         n=n+1
#     else:
#         p=p+1
#     i=i+1   
# print("positive num",p) 
# print("negative num",n) 
# 
a= [2, -7, 5, -64, -14]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]<0:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1   
print(b,len(b)) 
print(c,len(c))  


