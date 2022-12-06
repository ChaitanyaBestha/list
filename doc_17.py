# 1714 ==> [1*, 7, 1*, 4] ==> [2, 7, 2, 4]
# a=[1,7,1,4]
# i=0
# b=[]
# while i<len(a):
#     if i%2==0:
#         b.append(a[i]*2)
#     else:
#         b.append(a[i])    
#     i=i+1
# print(b)    
     
# # 12345 ==> [1, 2*, 3, 4*, 5] ==> [1, 4, 3, 8, 5]
# a=[1, 2, 3, 4, 5]
# i=0
# b=[]
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i]*2)
#     else:
#         b.append(a[i])    
#     i=i+1
# print(b) 
# 
 
# [8, 18*, 1] ==> [8, (18-9), 1] ==> [8, 9, 1]
a=[8,18,1]
i=0
b=[]
while i<len(a):
    if i%2!=0:
        b.append(a[i]-9)
    else:
        b.append(a[i])
    i=i+1
print(b)            
   