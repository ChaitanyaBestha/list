# a="my1 name is8 chaitu"
# i=0
# c=0
# while i<len(a):
#     d=a[i]
#     if d.isdigit()!=True:
#         c=c+1
#         print(d,end="")
#     i=i+1       


# a="my1 name is8 chaitu"
# i=0
# c=0
# while i<len(a):
#     d=a[i]
#     if d.isdigit()!=True:
#         c=c+1
#         print(d,end="")
#     i=i+1       

# a=[2,3,7,2,1,9,3,5,8,9,11,23]
# b=[1,7,9,11,23,4,5,7,8,9,2,3,12,9]
# i=0
# j=0
# d=[]
# c=[]
# while i<len(a) and j<len(b):
#     if a[i] not in c:
#         c.append(a[i])
#     if  b[i] not in d:
#         d.append(b[i])   
#     i=i+1
# print(c)
# print(d)
# i=0
# while i<len(d):
#     c.append(d[i])
#     i=i+1
# print(c)
# i=0
# e=[]
# while i<len(c):
#     if c[i] not in e:
#         e.append(c[i])
#     i=i+1
# print(e) 
# e.sort()
# print(e)           

a=[[[2,3,4],8,9,10],6,8]
i=0
sum1=0
while i<len(a):
    if type (a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    sum1+=a[i][j][k]
                    k=k+1
            else:
                sum1+=a[i][j]
            j=j+1
    else:
        sum1+=a[i]
    i=i+1
print(sum1)

