a=["one","two","three","four","five"]
i=0
b=[]
while i<len(a):
    c=str(i+1)+":"+a[i]
    b.append(c)
    i=i+1
print(b)    