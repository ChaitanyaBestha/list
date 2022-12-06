num=8
n=[1,2,3,4,5,6,7,8,9]
i=0
while i<len(n):
    j=i+1
    while j<len(n):
        if n[i]+n[j]==num:
            print(list((n[i],n[j])),end=" ")
        j=j+1
    i=i+1