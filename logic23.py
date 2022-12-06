a=[12300,1620,150,20,74820]

i=0
b=[]
e=[]
while i<len(a):
    c=str(a[i])
    b.append(c)
    # print(b[0][1])
    j=0
    d=""
    while j<len(b[i]):
        if b[i][j]!='0':
            d+=b[i][j]
        j+=1
    f=int(d)
    e.append(f)
       
    i=i+1
print(e)
    # c=a[i]//10
    # b.append(c)
# print(b)    
    