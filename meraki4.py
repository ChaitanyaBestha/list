# # List of numbers
# list1 = [50, 40, 23, 70, 56, 12, 5, 10, 7]

# # Removing duplicates from the list
# list2 = list(set(list1))

# # Sorting the  list
# list2.sort()

# # Printing the second last element
# print("Second largest element is:", list2[-2])
# print("second smallest element is:",list2[1])

l=[10,15,20,24,30,40]
max1=l[0]
max2=l[0]
min1=1000
min2=1000
for i in range(len(l)):
    if l[i]>max1:
        max1=l[i]
for j in range(len(l)):        
    if l[j]>max2 and l[j]!=max1:
        max2=l[j]    
for a in range(len(l)):
    if l[a]<min1:
        min1=l[a]
for m in range(len(l)) :       
    if l[m]<min2 and l[m]!=min1:
        min2=l[m]
print(max1)
print(max2)
print(min1)
print(min2)                    

