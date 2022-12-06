a=[5,6,[],3,[],[],9]
b=[]
i=0
while i<len(a):
    num=a[i]
    if a[i]==num and num!=[]:
        b.append(num)
    i=i+1
print(b)        