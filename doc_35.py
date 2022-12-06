a=[1234, 122, 1184, 19372, 100]
result=True
i=0
while i<len(a):
    b=str(a[i])
    if b[0]!=1:
        result=False
        break
    i=i+1
print(result)

        

# a=[1234, 922, 1984, 19372, 100]
# b=[]
# i=0
# while i<len(a):
#         c=str(a[i])
#         d=list(c)
#         b.append(d)
#         i=i+1
# print(b)
# if b[0][0] and b[1][0] and b[2][0] and b[3][0] and b[4][0]==1:
#     print("true")
# else:
#     print("false")

    

