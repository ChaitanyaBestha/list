list1=[6,1,3,5,6,3,1]
list2=[]
i=0
while i<len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i=i+1
print(list2)        
i=0
product=1
while i<len(list2):
    product=product*list2[i]
    i=i+1
print(product)    



