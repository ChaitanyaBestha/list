a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
b=""
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        b=b+a[i][j]
print(b)

