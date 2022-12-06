a=[4, 5, 5, 5, 3, 8]
# b=[]
# i=0
# while i<len(a):
#     c=a.count(a[i])
#     if c>=3:
#         if a[i] not in b:
#             b.append(a[i])
#     i=i+1
# print(b) 

a=[1, 1, 1, 64, 23, 64, 22, 22, 22]
b=[]
i=0
while i<len(a):
    c=a.count(a[i])
    if c>=3:
        if a[i] not in b:
            b.append(a[i])
    i=i+1
print(b) 


a=[1,2,3]
# for i in range(len(a)):
#     for j in range(len(a)):
#         for k in range(len(a)):
#             if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
#                 print(a[i],a[j],a[k])

            
