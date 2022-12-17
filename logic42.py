a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
i=0
b=[]
while i<len(a):
    c=(a[i],a[i+1],a[i+2])
    b.append(list(c))
    i=i+3
print(b)    
