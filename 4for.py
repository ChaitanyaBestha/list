list1=[6,1,3,5,6,3,1]
list2=[]
for i in range(0,len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(list2)        
product=1
for i in range(0,len(list2)):
    product=product*list2[i]
print(product)    



