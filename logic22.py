a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
# output:-[['a','d','g','j','m'],['b','e','h','k','n'],['c','f','i','l']]
i=0
b=[]
n=int(input("enter no:"))
while i<n:
    j=i
    c=[]
    while j<len(a):
        d=a[j]
        c.append(d)
        
        j=j+n
   
    b.append(c)
    
    i=i+1
print(b)
# print(b)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              :
    