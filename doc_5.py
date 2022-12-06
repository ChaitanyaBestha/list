l = [1, 2, 2, 5, 8, 4, 4, 8]
m=[]
i=0
while i<len(l):
    if l[i] not in m:
        m.append(l[i])
    i=i+1
print(m)
print(len(m))         