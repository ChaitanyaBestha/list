# a=[2,-4,5,-1,-6,8,9]
# i=0
# even=[]
# odd=[]
# even1=0
# odd1=0
# while i<len(a):
#     if a[i]>0:
#         even1=even1+1
#         even.append(a[i])
#     else:
#         odd1=odd1+1 
#         odd.append(a[i])
#     i=i+1
# print(even1,even)
# print(odd1,odd)           

# a=["ashu","3",5,4.5,2,8.0]
# i=0
# b=[]
# c=[]
# d=[]
# while i<len(a):
#     if type(a[i])==str:
#         b.append(a[i])
#     elif type(a[i])==int:
#         c.append(a[i])
#     else:
#         d.append(a[i])
#     i=i+1
# print(b)
# print(c)                
# print(d)                


# a=int(input("list numbers"))
# b=str(a)
# i=0
# c=[]
# while i<len(b):
#     c.append(int(b[i]))
#     i=i+1
# print(c)
# i=0
# b=[]
# d=[]
# while i<len(c):
#     if c[i]%2==0:
#         b.append(c[i])
#     else:
#         d.append(c[i])
#     i=i+1
# print(b)
# print(d)            



# # e=0
# # o=0
# # while a>0:
# #     # if a[i]%2==0:
# #     #     b.append(a[i])
# #     # else:
# #     #     c.append(a[i])
# #     # i=i+1
# #     b=a%10
# #     a=a//10
# #     if b%2==0:
# #         print(b,end=" ")
# #         e=e+1
# #     if b%2!=0:
# #         print(b,end=" ")
# #         o=o+1
# # print(e)
# # print(o)        
                


# # # a=[24]
# # # i=0
# # # while i<len(a):
# # #     j=0
# # #     while a[i]>0:
# # #         b=a[i]%10
# # #         j=j+b
# # #         a[i]=a[i]//10
# #     # i=i+1 
# # # print(j)  

# # a=int(input())
# # j=0
# # while a>0:
# #     b=a%10
# #     j=j+b
# #     a=a//10     
# if j%2==0:
#     print("even")
# else:
#     print("odd")    

# a=[(123456789)]
# b=str(a)
# # print(b)
# c=b[1:4]
# d=b[4:7]
# e=b[7:10]
# print("("+c+")"+d+"-"+e)

# a=[1,2,3,4,5]
# b=[2,3,1,0,6,7]
# i=0
# c=[]
# while i<len(a):
#     if a[i] not in b :
#         c.append(a[i])
#     i=i+1
# print(c)    

# room=[1,2,3,4]
# a=["rama","nene","mama","nana"]
# b=["kaka","macha","chacha","baapu"]
# i=0
# j=0
# while i<len(a):
#     print("room",room[i])
#     print(" "+"1",a[i],"\n","2",b[j])
#     i=i+1
#     j=j+1
    
# a=[1,2,3,4,5,7]
# i=0
# j=1
# d=[]
# while i<len(a):
#     b=a[i]+j
#     c=b%10
#     d.append(c)
#     i=i+1
#     j=j+1
# print(d)    

# a=[['a','s'],['h','w','i'],['n','i']]
# i=0
# b=""
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b=b+a[i][j]
#         j=j+1
#     i=i+1
# print(b) 
# i=0
# while i<len(b): 
#     c=b.capitalize()
#     i=i+1
# print(c)    






# a=['ice','cream']
# i=0
# b=[]
# while i<len(a):
#     c=a[i].capitalize()
#     b.append(c)
#     i=i+1
# e=''.join(b)
# print(e)



    


# a="anjali"
# i=0
# # b=[]
# while i<len(a):
#     c=a[i]*5
#     # b.append(c)
#     i=i+1
#     print(c,end=" ")    
 
# a=['a','b','n','a','x','c','x']
# i=0
# c=[]
# while i<len(a):
#     b=a.count(a[i])
#     if b>1:
#         d=(a[i],b)
#         if d not in c:
#             c.append(d)
#     else:
#         c.append(a[i])
#     i=i+1
# print(c)                

# a=[12,13,15,16,17]
# i=0
# b=[]
# while i<len(a):
#     sum=0
#     while a[i]>0:
#         sum=sum+a[i]%10
#         a[i]=a[i]//10
#     i+=1
#     b.append(sum)
# print(b)

# a="()[]{}"
# n=input("enter character:")
# if n in a:
#     print("true")
# else:
#     print("false")    

# a=["mukti","Devika","chaitanya"]
# n=input("enter character:")
# i=0
# while i<len(a):
#     if a[i][0]==n:
#         print(a[i])
#     i=i+1  

# a=['one','two','three','four','five'] 
# i=0
# b=[]
# while i<len(a):
#     c=str(i+1)+":"+a[i]
#     b.append(c)
#     i=i+1
# print(b)     

# a=[100,12,34,2,1233,45,67,56,78]
# i=0
# max1=0
# max2=0
# max3=0
# while i<len(a):
#     if a[i]>max1:
#         max1=a[i]
#     i=i+1
# print(max1)  
# j=0
# while j<len(a):
#     if a[j]>max2 and a[j]!=max1:
#         max2=a[j] 
#     j=j+1
# print(max2)    
# k=0
# while k<len(a):
#     if a[k]>max3 and a[k]!=max1 and a[k]!=max2:
#         max3=a[k]
#     k=k+1
# print(max3)                 

# a=[12,23,234,345,34,56,78]
# i=0
# b=[]
# while i<len(a):
#     sum=0
#     while a[i]>0:
#         sum=sum+a[i]%10
#         a[i]=a[i]//10
#     i=i+1
#     b.append(sum)
# print(b)    

# a=['a','b','c']
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i!=j and j!=k and k!=i :
#                 print(a[i],a[j],a[k])

a=['2','3','4','5']
b=['amp']
i=0
c=[]
while i<len(a):
    c.append(a[i]+b[0])
    i=i+1
print(c)    