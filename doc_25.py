# # creating the array
# arr = [4, 5, 5, 5, 3, 8]
  
# # size of the list
# size = len(arr)
  
# # looping till length - 2
# for i in range(size - 2):
  
#     # checking the conditions
#     if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
  
#         # printing the element as the 
#         # conditions are satisfied 
#         print(arr[i])


# a=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# b=[]
# i=0
# while i<len(a):
#     c=a.count(a[i])
#     if c>=3:
#         if a[i] not in b:
#             b.append(a[i])
#     i=i+1
# print(b)        
a=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
b=[]
i=0
while i<len(a):
    c=a.count(a[i])
    if c>=3:
        if a[i] not in b:
            b.append(a[i])
    i=i+1
print(b)