
a='aabcddddadnss'
i=0
c=[]
while i<len(a):
    b=a.count(a[i])
    if b>=1:
        d=[a[i],b]
        if d not in c:
            c.append(d)
    else:
        c.append(a[i])
    i=i+1
print(c)

# a=[1, 1, 2, 3, 4, 4, 5, 1]
# i=0
# b=[]
# while i<len(a)-1:
#     if a[i]==a[i+1]:
#         d=[a[i],2]
#         b.append(d)
#     else:
#         b.append(a[i])
#     i=i+2
# print(b)

# i=1
# while i<=10:
#     print(i)
#     i=i+1

# i=0
# while i<10:
#     i=i+1
#     if i==5 or i==6:
#         print( )
#         continue
#     print(i)

# i=0
# while i<10:
#     i=i+1
#     continue
#     if i==5 or i==6:
#         # continue
#         print( )
#         # continue
#     print(i)
    
# i=0
# while i<10:
#     # i=i+1
#     if i==5 or i==6:
#         print( )
#         continue
#     print(i)
#     i=i+1
# i=0
# while i<10:
#     if i==5 or i==6:
#         print( )
#         continue
#     i=i+1
#     print(i)
# i=0
# while i<10:
#     # i=i+1
#     continue
#     i=i+1
#     print(i)
#     # continue
#     if i==5 or i==6:
#         print( )
#         # continue
#     # print(i)
# i=1
# while i<=10:
#     if i==4 and i==6:
#         break
#     else:
#         print(i)
#     i=i+1    