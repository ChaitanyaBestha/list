
user=int(input("enter the size:"))
i=0
b=[]
while i<user:
    a=int(input("enter the num:"))
    i=i+1
    b.append(a)
k=0
while k<user:
    j=0
    while j<(user-1):
        if b[j]>b[j+1]:
            c=b[j]
            b[j]=b[j+1]
            b[j+1]=c
        j+=1
    k+=1
print("bubble sort")
print(b)

# list=[3,10,111,23,45,14]
# i=0
# while i<len(list):
#     j=0
#     while j<(len(list)-1):
#         if list[j]>list[j+1]:
#             c=list[j]
#             list[j]=list[j+1]
#             list[j+1]=c
#         j+=1
#     i+=1
# print("bubble sort")
# print(list)