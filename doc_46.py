a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
i=0
d=[]
while i<len(a):
    n=a[i]+b[i]+c[i]
    d.append(n)
    i=i+1
print(d)    
