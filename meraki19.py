l=[23,14,56,12,19,9,15,25,31,42,43]
sumodd=0
sumeven=0
odd=[]
even=[]
allnumbersum=0
l2=len(l)
i=0
while i<len(l):
    allnumbersum+=l[i]
    if(l[i]%2==0):
        sumeven+=l[i]
        even.append(l[i])
        length=len(even)
    else:
        sumodd+=l[i]
        odd.append(l[i])
        l1=len(odd)
    i=i+1   
print("Count of odd numbers=",l1)
print("Count of even numbers=",length)
print("Count of all the numbers=",len(l))
print("Sum of odd numbers=",sumodd)
print("Sum of even numbers=",sumeven)
print("Sum of all the numbers=",allnumbersum)
print("Average of odd numbers=",sumodd/l1)
print("Average of even numbers=",sumeven/length)
print("Average of all numbers=",allnumbersum/l2)

