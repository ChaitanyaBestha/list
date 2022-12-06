# a=[1,2,3,4,5,6]
# i=0
# j=-1
# b=[]
# while i<len(a)-3:
#     # c=a[j],a[i]
#     b.append(a[j])
#     b.append(a[i])
#     i=i+1
#     j=j-1
# print(b)    
a=[[4,2,1],[2,2,3],[5,5,2]]
c=[]

i=0
while i<len(a):
    j=0
    sum1=0
    while j<len(a):
        sum1=sum1+a[i][j]
        j=j+1
    c.append(sum1)
    i=i+1
print(c)        
