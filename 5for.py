l = [1, 2, 2, 5, 8, 4, 4, 8]
m=[]
for i in range(0,len(l)):
    if l[i] not in m:
        m.append(l[i])
    i=i+1
print(m)
print(len(m))         